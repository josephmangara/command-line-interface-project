"""changed to reder model and added staff model

Revision ID: 3b0cc9b16386
Revises: 58d266508d30
Create Date: 2024-01-11 01:53:58.349780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b0cc9b16386'
down_revision = '58d266508d30'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('contact_info', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.Column('contact_info', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('staff')
    op.drop_table('readers')
    # ### end Alembic commands ###