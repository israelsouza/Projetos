const botoesCarrossel = document.querySelectorAll('.btn');
const imagens = document.querySelectorAll('.imagemC');

botoesCarrossel.forEach((botao, index) => {
    botao.addEventListener('click', () => {
        desativarClasseBotao();
        addClasseBotao(botao);
        
        esconderImagemFundo();
        mostrarImagemFundo(index);
    });
});

function mostrarImagemFundo(index) {
    imagens[index].classList.add('ativa');
}

function esconderImagemFundo() {
    const imagemFundo = document.querySelector('.ativa');
    imagemFundo.classList.remove('ativa');
}

function addClasseBotao(botao) {
    botao.classList.add('selecionado');
}

function desativarClasseBotao() {
    const botaoSelecionado = document.querySelector('.selecionado');
    botaoSelecionado.classList.remove('selecionado');
}