"""Initial migration

Revision ID: 6cd3e8a0b214
Revises: 0bc03b7bd495
Create Date: 2024-08-27 11:56:24.569079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cd3e8a0b214'
down_revision: Union[str, None] = '0bc03b7bd495'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###