"""Added three models

Revision ID: 58d266508d30
Revises: 680aa5bb4d19
Create Date: 2024-01-10 13:12:46.943732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58d266508d30'
down_revision = '680aa5bb4d19'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('edition', sa.String(), nullable=True),
    sa.Column('condition', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libraries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('contact_info', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('libraries')
    op.drop_table('books')
    # ### end Alembic commands ###