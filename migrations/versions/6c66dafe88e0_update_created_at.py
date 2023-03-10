"""update created_at

Revision ID: 6c66dafe88e0
Revises: 46b9c4e10e02
Create Date: 2023-01-23 19:39:18.579091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6c66dafe88e0'
down_revision = '46b9c4e10e02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drones', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.drop_column('drones', 'created-at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drones', sa.Column('created-at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True))
    op.drop_column('drones', 'created_at')
    # ### end Alembic commands ###
