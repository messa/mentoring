console.info('JS v samostatnem souboru')

function udelatOddstavecCerveny() {
    const element = document.getElementById('o2');
    element.style.color = 'red';

    element.innerText += 'UPRAVENO';

    var para = document.createElement("p");
    var node = document.createTextNode("This is new.");
    para.appendChild(node);
    element.appendChild(para);
}

