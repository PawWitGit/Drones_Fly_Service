"""Initial

Revision ID: 591c28449bc1
Revises: 
Create Date: 2023-01-21 23:44:41.659186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "591c28449bc1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=True),
        sa.Column("password", sa.String(length=260), nullable=True),
        sa.Column("login", sa.String(length=150), nullable=True),
        sa.Column("first_name", sa.String(length=200), nullable=True),
        sa.Column("last_name", sa.String(length=200), nullable=True),
        sa.Column("role", sa.Enum("admin", "user", name="roletype"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "drones",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("manufacturer", sa.String(length=120), nullable=False),
        sa.Column("description", sa.String(length=1000), nullable=False),
        sa.Column("model", sa.String(length=200), nullable=False),
        sa.Column("drone_type", sa.String(length=120), nullable=False),
        sa.Column(
            "created-at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("photo_url", sa.String(length=120), nullable=False),
        sa.Column(
            "status",
            sa.Enum("created", "edited", "deleted", name="state"),
            nullable=False,
        ),
        sa.Column("drone_pilot_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["drone_pilot_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("drones")
    op.drop_table("users")
    # ### end Alembic commands ###