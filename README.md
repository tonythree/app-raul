# app-raul

1. Registrarte en github

2. crear repositorio nuevo (publico).

3. instalar Git en tu ordenador (en el terminal). https://git-scm.com/download/win

4. Clonar repositorio -> copias la url desde el github (HTTPS) y haces:
```
git clone <url>
```
  
5. Intentas hacer un cambio o añadir un fichero y lo subes a tu propio git haciendo:  
```
git add . 
git commit -m "mensaje"
git push
```


--------


6. Python: crear nuevo virtualenv dentro de la carpeta del repositorio de git. 
```
python3 -m venv venv
```

7. Activar el virtualenv -> 
```
venv\Scripts\activate.bat
```

8. Recuerda, para desactivarlo -> 
```
deactivate
```

9. Instalar flask dentro del virtualenv -> 
```
pip install flask
```

10. compruebas que se ha instalado correctamente -> 
```
pip freeze
```

11. creas tu nuevo app.py o como quieras llamarlo y metes la info. Puedes mirar como referencia: https://github.com/tonythree/app-raul

12. Para correr una app en flask
```
flask run
```
