from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate



router = APIRouter(
    prefix='/operations',
    tags=["Operation"]
)


@router.get("/")
async def get_spec_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        operations = list(result.mappings())
        return {
            'status': 'success',
            'data': operations,
            'details': None
        }
    except:
        raise HTTPException(status_code=400, detail={
            'status': '400',
            'details': 'Операция не найдена.'
        })




@router.post("/")
async def add_spec_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            'status': 'success',
            'data': stmt,
            'details': None,
        }
    except:
        return {
            'status': 'error',
            'data': None,
            'details': None
        }