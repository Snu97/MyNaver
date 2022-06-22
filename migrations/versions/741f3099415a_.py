"""empty message

Revision ID: 741f3099415a
Revises: c642e6ddd6cd
Create Date: 2021-08-10 12:33:45.609438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '741f3099415a'
down_revision = 'c642e6ddd6cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('novel', sa.Column('create_date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('novel', 'create_date')
    # ### end Alembic commands ###
