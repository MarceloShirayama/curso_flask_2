## Contextos

```python
from flask import Flask

app = Flask(__name__)  
``` 
app é um objeto da instância classe Flask ele tem  todos os  métodos que o Flask implementa.

### 1 - Configuração

Add configuração
```python
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://..."
```

 Registrar Rotas

 ```python
@app.route("/path")
def funcao():
    ...

app.add_url_rule("/path", callable)
```

 Inicializar extensões

```python
from flask_admin import Admin
Admin.init_app(app)
```

 Registrar Blueprints

```python
app.register_blueprints(...)
```

 add hooks

```python
@app.before_request(...)
@app.error_handler(...)
```

 Chamar outras factories

```python
views.init_app(app)
```

### 2 - App Context

 App está pronto! `app`
-    Testar
-   app.test_client
-   debug
-   objetos globais do Flask
-   (importar request, session, g)
-   Hooks

```python
from flask import current_app, g
```

### 3 - Request Context

 usar globais do flask

```python
from flask import request, session, g

request.args
request.form
```