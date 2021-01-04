"""empty message

Revision ID: 98a370521aa5
Revises: 2425abece127
Create Date: 2020-12-27 20:06:05.431542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98a370521aa5'
down_revision = '2425abece127'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car_carpark_geometry', sa.Column('easting', sa.String(length=50), nullable=True))
    op.add_column('car_carpark_geometry', sa.Column('northing', sa.String(length=50), nullable=True))
    op.add_column('heavy_vehicle_carpark_geometry', sa.Column('easting', sa.String(length=50), nullable=True))
    op.add_column('heavy_vehicle_carpark_geometry', sa.Column('northing', sa.String(length=50), nullable=True))
    op.add_column('motor_bike_carpark_geometry', sa.Column('easting', sa.String(length=50), nullable=True))
    op.add_column('motor_bike_carpark_geometry', sa.Column('northing', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('motor_bike_carpark_geometry', 'northing')
    op.drop_column('motor_bike_carpark_geometry', 'easting')
    op.drop_column('heavy_vehicle_carpark_geometry', 'northing')
    op.drop_column('heavy_vehicle_carpark_geometry', 'easting')
    op.drop_column('car_carpark_geometry', 'northing')
    op.drop_column('car_carpark_geometry', 'easting')
    # ### end Alembic commands ###
