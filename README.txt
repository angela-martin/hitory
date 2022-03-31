Hitori puzzle

Para compilar el código:

1) Ejecutar 'conda activate' en la terminal para poder llamar a clingo.

2) Existe un Makefile con las opciones: [PARA SELECCIONAR EL FICHERO hitoriX.txt A RESOLVER CAMBIAR LA VARIABLE 'NUMFILE' EN EL MAKEFILE]
	
	- make encode: ejecuta el fichero encode.py que crea el fichero hitoriX.lp con los hechos del problema.

	- make decode: ejecuta el fichero decode.py que crea el fichero merge.lp (hitoriX.lp + hitoriKB.lp) y solutionX.lp con la solución.

	- make solve: ejecuta encode.py y decode.py, obtiene la solución (lo mismo que hacer make encode y luego make decode).

	- make clean: elimina los ficheros creados durante la ejecución.
