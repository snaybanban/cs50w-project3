# Project 3

Web Programming with Python and JavaScript

Este proyecto consiste en una app para una pizzería que admite la compra de sus productos en línea, el usuario podrá ver el meno y ver los diferentes precios, tamaños y sabores.
Al iniciar la app, al usuario se le mostrará la página de iniciar sesión si ya está registrado podrá iniciar normal al home Page, si no podrá registrarse como nuevo usuario. Al logearse bien, se le mostrara el menú de los productos, cada uno dependiendo de su sección. El usuario podrá añadir a su carrito cualquiera, tendrá la facilidad de agrandar su orden o elegir diferentes ingredientes si el caso es pizza.
Al momento de añadir el producto al carrito, el usuario podrá ver su pedido, el precio a pagar, tamaño y podrá incluso cancelarla, si no es así podrá ver la lista de sus pedidos.


Vistas


	Cart: en ella se mostrará las ordenes añadidas y en ella se verá y podrá dar por completado el producto.
	Comparar: acá se mostrará la comparativa sobre las pizzas siciliana y regular.
	Contacto: so mostrara información del local.
	Horas: acá se mostrará los horarios de atención.
	Index: en ella se mostrará todo el cuerpo del menú principal.
	Layout: esta es la ruta madre para todas las urls de la app.
	Login: será para iniciar sesión (se un forms para la sesión de Django).
	Logout: para cerrar sesiones.
	Orders: acá se mostrará una lista detallada de cada pedido ya realizado con un historial, en el estará día, hora, precio, tamaño del producto.
	Post: esta ruta se le mostrará al usuario administrador, en ella podrá incluir anuncios en tiempo real para sus clientes.
	Profile: esta ruta de será mostrada para los administradores, acá saldrán información al admin de sus anuncios en la pagina y desde acá podrá acceder al panel de admin en Django.
	Register: esta ruta será para registrar un nuevo usuario.
	Vieworders: esta ruta solo será visible para los administradores. Acá el admin podrá ver las ordenes solicitadas por sus clientes, podrá ver el nombre del usuario, el servicio adquirido, información de día y hora y su precio. También podrá marcar como completada.
 


Toque personal:
Se implemento el postear anuncios, para mostrárselos a los usuarios al momento de estar logeados.
El usuario staff, podrá ver todas las ordenes de sus clientes y marcarlas como terminadas.
