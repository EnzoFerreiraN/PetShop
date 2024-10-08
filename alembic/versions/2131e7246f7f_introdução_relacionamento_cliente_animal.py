"""Introdução Relacionamento cLiente-Animal

Revision ID: 2131e7246f7f
Revises: 4fab137ca2ca
Create Date: 2024-09-03 12:36:49.860074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2131e7246f7f'
down_revision: Union[str, None] = '4fab137ca2ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('especie', sa.String(), nullable=True),
    sa.Column('raca', sa.String(), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], name='fk_cliente_id'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('animais', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_animais_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animais', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_animais_id'))

    op.drop_table('animais')
    # ### end Alembic commands ###
