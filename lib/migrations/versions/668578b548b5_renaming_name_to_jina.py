"""Renaming name to jina 

Revision ID: 668578b548b5
Revises: 8a6ebdc9d0b6
Create Date: 2023-09-05 07:39:54.258945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '668578b548b5'
down_revision = '8a6ebdc9d0b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars','name',new_column_name='jina')


def downgrade() -> None:
    op.alter_column('scholars','jina',new_column_name='name')
    
