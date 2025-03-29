import os

#obtener el entrada
valor = os.environ.get("INPUT_VAL")

#mostrar resultado en consola 
if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            print("{0} = hola {1}".format("result",valor), file=f)