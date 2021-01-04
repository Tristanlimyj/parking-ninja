"""empty message

Revision ID: 51d4b97d7483
Revises: 2a0c858cb838
Create Date: 2020-12-31 02:53:47.698417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51d4b97d7483'
down_revision = '2a0c858cb838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_system_response', 'message_body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_system_response', sa.Column('message_body', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
