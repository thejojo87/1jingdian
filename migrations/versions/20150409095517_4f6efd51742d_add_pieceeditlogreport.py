"""Add PieceEditLogReport.

Revision ID: 4f6efd51742d
Revises: 319e8e7d746a
Create Date: 2015-04-09 09:55:17.676959

"""

# revision identifiers, used by Alembic.
revision = '4f6efd51742d'
down_revision = '319e8e7d746a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('piece_edit_log_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('piece_edit_log_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['piece_edit_log_id'], ['piece.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('piece_edit_log_report')
    ### end Alembic commands ###
