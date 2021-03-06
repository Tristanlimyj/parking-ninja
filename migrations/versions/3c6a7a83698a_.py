"""empty message

Revision ID: 3c6a7a83698a
Revises: 98a370521aa5
Create Date: 2020-12-28 16:58:37.190427

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3c6a7a83698a'
down_revision = '98a370521aa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('update_id', sa.Integer(), nullable=True),
    sa.Column('message_body', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_info')
    # ### end Alembic commands ###
