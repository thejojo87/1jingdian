"""Add processed to CollectionEditLogReport.

Revision ID: 505e944a76a9
Revises: 4b9970e8b566
Create Date: 2015-04-11 17:51:51.338663

"""

# revision identifiers, used by Alembic.
revision = '505e944a76a9'
down_revision = '4b9970e8b566'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection_edit_log_report', sa.Column('processed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('collection_edit_log_report', 'processed')
    ### end Alembic commands ###
