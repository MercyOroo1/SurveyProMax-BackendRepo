"""renaming password

Revision ID: 700a8af61e1e
Revises: 3e1e2f9a2ca2
Create Date: 2024-07-09 15:05:28.702231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700a8af61e1e'
down_revision = '3e1e2f9a2ca2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('answer', sa.String(length=1), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=255), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('password_hash')

    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.drop_column('answer')

    # ### end Alembic commands ###
