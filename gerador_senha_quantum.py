from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import transpile
from qiskit.providers.aer import QasmSimulator

n_binario = 7
tamanho_senha = 8
senha = list()
limit = [32,126]
senha_normal = ""
controlador_loop = tamanho_senha

qubits = QuantumRegister(n_binario)
bits = ClassicalRegister(n_binario)

circuito_quantico = QuantumCircuit(qubits, bits)

#aplica a porta Hadamard(superposição)
for i in range(n_binario):
    circuito_quantico.h(qubits[i])

#medição em 0 ou 1
for i in range(n_binario):
    circuito_quantico.measure(qubits[i],bits[i])

def simulador_quantico(circuito_quantico):
    backend = QasmSimulator()
    qc_compiled = transpile(circuito_quantico, backend)
    job = backend.run(qc_compiled, shots = 1024)
    result = job.result()
    counts = result.get_counts()

    max_key = max(counts, key=lambda key: counts[key])
    return int(max_key,2)
    

for i in range(tamanho_senha):
    while(controlador_loop != 0):
        inteiro = simulador_quantico(circuito_quantico)
        if inteiro >= limit[0] and inteiro <= limit[1]:
            senha.append(chr(inteiro))  
            senha_normal += chr(inteiro)  
            controlador_loop -= 1
        
print("Senha: " + str(senha))
print("Senha normal: " + senha_normal)





