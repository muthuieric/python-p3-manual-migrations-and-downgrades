"""Renaming students to scholars

Revision ID: 8a6ebdc9d0b6
Revises: 791279dd0760
Create Date: 2023-09-05 07:23:21.499544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a6ebdc9d0b6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
