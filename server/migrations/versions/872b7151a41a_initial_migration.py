"""Initial migration.

Revision ID: 872b7151a41a
Revises: 
Create Date: 2024-07-08 22:33:23.090073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872b7151a41a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
