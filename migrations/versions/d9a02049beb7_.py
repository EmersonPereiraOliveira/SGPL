"""empty message

Revision ID: d9a02049beb7
Revises: 
Create Date: 2018-03-25 14:49:14.450080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9a02049beb7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fornecedor_fornece_produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fornecedor', sa.Integer(), nullable=True),
    sa.Column('produto', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fornecedor'], ['fornecedores.id'], ),
    sa.ForeignKeyConstraint(['produto'], ['produtos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fornecedores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('razao_social', sa.String(length=50), nullable=True),
    sa.Column('nome_fantasia', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('cnpj', sa.String(length=11), nullable=True),
    sa.Column('telefone', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itens_do_pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('fornecedor_1', sa.Integer(), nullable=True),
    sa.Column('fornecedor_2', sa.Integer(), nullable=True),
    sa.Column('fornecedor_3', sa.Integer(), nullable=True),
    sa.Column('valor_fornecedor_1', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('valor_fornecedor_2', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('valor_fornecedor_3', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('pedido', sa.Integer(), nullable=True),
    sa.Column('produto', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fornecedor_1'], ['fornecedores.id'], ),
    sa.ForeignKeyConstraint(['fornecedor_2'], ['fornecedores.id'], ),
    sa.ForeignKeyConstraint(['fornecedor_3'], ['fornecedores.id'], ),
    sa.ForeignKeyConstraint(['pedido'], ['pedidos.id'], ),
    sa.ForeignKeyConstraint(['produto'], ['produtos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido_tem_item_do_pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pedido', sa.Integer(), nullable=True),
    sa.Column('item_do_pedido', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_do_pedido'], ['itens_do_pedido.id'], ),
    sa.ForeignKeyConstraint(['pedido'], ['pedidos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=50), nullable=True),
    sa.Column('requisitante', sa.Integer(), nullable=True),
    sa.Column('itens', sa.Integer(), nullable=True),
    sa.Column('usuario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['itens'], ['itens_do_pedido.id'], ),
    sa.ForeignKeyConstraint(['requisitante'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['usuario'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pregoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pedido', sa.Integer(), nullable=True),
    sa.Column('requisitante', sa.Integer(), nullable=True),
    sa.Column('usuario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pedido'], ['pedidos.id'], ),
    sa.ForeignKeyConstraint(['requisitante'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['usuario'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('catmat', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('setores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha', sa.String(length=50), nullable=True),
    sa.Column('setor', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.Integer(), nullable=True),
    sa.Column('tipo2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['setor'], ['setores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    op.drop_table('setores')
    op.drop_table('produtos')
    op.drop_table('pregoes')
    op.drop_table('pedidos')
    op.drop_table('pedido_tem_item_do_pedido')
    op.drop_table('itens_do_pedido')
    op.drop_table('fornecedores')
    op.drop_table('fornecedor_fornece_produto')
    # ### end Alembic commands ###