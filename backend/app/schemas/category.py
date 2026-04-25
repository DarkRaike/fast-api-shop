from pydantic import BaseModel, Field


class CategoryBase(BaseModel):  # ОБЩИЕ поля для остальных моделей
    name: str = Field(..., min_length=5, max_length=100, description="Category name")
    slug: str = Field(
        ..., min_length=5, max_length=100, description="URL-friendly category name"
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):  # для просмотра детальной информации о категории
    id: int = Field(
        ..., description="Unique category identifier"
    )  # ... значит, что обязательное поле

    class Config:
        from_attributes = True  # позволяет создавать схему напрямую из модели
