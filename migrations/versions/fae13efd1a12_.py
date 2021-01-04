"""empty message

Revision ID: fae13efd1a12
Revises: f3f93dc7a5df
Create Date: 2020-12-26 23:45:27.274568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fae13efd1a12'
down_revision = 'f3f93dc7a5df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car_available_lot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_table_id', sa.Integer(), nullable=False),
    sa.Column('lots_available', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['main_table_id'], ['car_carpark_main_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heavy_vehicle_available_lot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_table_id', sa.Integer(), nullable=False),
    sa.Column('lots_available', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['main_table_id'], ['heavy_vehicle_carpark_main_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motor_bike_available_lot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_table_id', sa.Integer(), nullable=False),
    sa.Column('lots_available', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['main_table_id'], ['motor_bike_carpark_main_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('motor_bike_available_lot')
    op.drop_table('heavy_vehicle_available_lot')
    op.drop_table('car_available_lot')
    # ### end Alembic commands ###