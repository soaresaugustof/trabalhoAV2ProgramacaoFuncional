path = "usuarios.txt"

save = open(path, "a")
search = open(path, "r")

salvar_usuario = lambda usuario: save.write(usuario + '\n')

buscar_usuario = lambda nome: [line for line in search if (nome in line)]

usuario1 = "Augusto, 30, augusto@email"
usuario2 = "Augusto, 25, augusto@email"
salvar_usuario(usuario1)
salvar_usuario(usuario2)

usuario_encontrado = buscar_usuario('Augusto')

print(usuario_encontrado)