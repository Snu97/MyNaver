"""empty message

Revision ID: 44cd220c393a
Revises: 84ddaab4d0b0
Create Date: 2021-08-29 17:36:11.179836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44cd220c393a'
down_revision = '84ddaab4d0b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('number', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('number', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
