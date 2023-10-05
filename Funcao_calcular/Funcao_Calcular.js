//Nome: Leonardo Saconato de Santana
//Turma: 08

//Programa Função Calculadora

function calculadora() {
  const num1 = parseFloat(prompt("Digite o primeiro número:"));
  const num2 = parseFloat(prompt("Digite o segundo número:"));
  const operacao = parseInt(prompt("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão):"));

  switch (operacao) {
    case 1:
      alert(`Resultado: ${num1 + num2}`);
      break;
    case 2:
      alert(`Resultado: ${num1 - num2}`);
      break;
    case 3:
      alert(`Resultado: ${num1 * num2}`);
      break;
    case 4:
      if (num2 !== 0) {
        alert(`Resultado: ${num1 / num2}`);
      } else {
        alert("Divisão por zero não é permitida.");
      }
      break;
    default:
      alert("Operação inválida. O resultado é 0.");
  }
}

// Chama a função calculadora para que o usuário insira os valores e a operação desejada
calculadora();
