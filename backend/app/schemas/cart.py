from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel): # получение информации о товаре из корзины
    product_id: int = Field(..., description='Product ID')
    quantity: int = Field(..., gt=0, description='Quantity (must be greater than 0)')
    
    
# перекидывание сессионной корзины на фронтенд это правильное решение
class CartItemCreate(CartItemBase):
    pass
    
class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description='Product ID')
    quantity: int = Field(..., gt=0, description='New quantity (must be greater than 0)')
    
class CartItem(BaseModel): # полноценная информация для вывода информации о товаре в корзине
    product_id: int = Field(..., description='Product ID')
    name: str = Field(..., description='Product name')
    price: float = Field(..., description='Product price')
    quantity: int = Field(..., gt=0, description='Quantity (must be greater than 0)')
    subtotal: float = Field(..., description='Subtotal (quantity * price)')
    image_url: Optional[str] = Field(None, description='Product image URL')
    
class CartResponse(BaseModel): # это список
    items: list[CartItem] = Field(..., description='List of items in cart') # массив из CartItem
    total: float = Field(..., description='Total cart price')
    items_count: int = Field(..., description='Total number of items in cart')
    
    