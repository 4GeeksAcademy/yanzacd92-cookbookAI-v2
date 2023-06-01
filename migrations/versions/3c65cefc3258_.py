"""empty message

Revision ID: 3c65cefc3258
Revises: 77a60dd94502
Create Date: 2023-05-30 02:55:46.610286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c65cefc3258'
down_revision = '77a60dd94502'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token_blocked_list', schema=None) as batch_op:
        batch_op.alter_column('jti',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token_blocked_list', schema=None) as batch_op:
        batch_op.alter_column('jti',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
