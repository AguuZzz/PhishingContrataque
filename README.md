
# Contraataque hacia phishing

Un script hecho en Python para devolver valores aleatorios a formularios de paginas phishing



## Requerimientos

Se necesita instalar el modulo request para correr el script

```bash
python -m pip install requests
```
    
## Uso

Para utilizar la herramienta se debera copiar el valor de "name="

```HTML
<form method="post">
    <input type="text" name="usuario">
    <input type="text" name="contraseña">
    <input type="submit">
</form>
```
En este caso los valores son "usuario" y "contraseña"

