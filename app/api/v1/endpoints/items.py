from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session

# from app import schemas

router = APIRouter()


@router.get("/", response_model=schemas.Item)
def read_items(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve items.
    """

    return [1, 2, 3]
#
#
# @router.post("/", response_model=schemas.Item)
# def create_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     item_in: schemas.ItemCreate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Create new item.
#     """
#     item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
#     return item
#
#
# @router.put("/{id}", response_model=schemas.Item)
# def update_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     item_in: schemas.ItemUpdate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
#     return item
#
#
# @router.get("/{id}", response_model=schemas.Item)
# def read_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get item by ID.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return item
#
#
# @router.delete("/{id}", response_model=schemas.Item)
# def delete_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.remove(db=db, id=id)
#     return item