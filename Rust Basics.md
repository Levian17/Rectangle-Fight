# Rust Basics

Conceptos indispensables
---
-   Es necesario el uso de `;` al final de las sentencias para indicar el final de una línea.
-   Es un lenguaje de tipado estático, por lo que cada variable recibe un tipo al ser declarada.
-   La creación básica de una variable se realiza con _`let`_, lo que crea una variable a la que se le debe asignar un valor. Las variables no poseen mutabilidad a menos que se especifique en su declaración con la palabra clave _`mut`_.

Ejemplo de una declaración de variable: 
`let mut value: f32 = 3.0;`

Esta declaración crea una variable mutable de tipo `f32` (un número de punto flotante de 32 bits).

Otra forma de declarar variables es empleando las palabras clave _`const`_ y _`static`_, que permiten declarar variables que se mantendrán constantes a lo largo de la ejecución. Existen diferencias entre _`const`_ y _`static`_, pero, simplificándolas, se puede decir que _`static`_ tiene una dirección de memoria fija.

Las variables constantes y estáticas deben estar capitalizadas.

Ejemplo de una declaración de variable constante y estática:
`const C: f32 = 3.0;`
`static S: f32 = 3.0;`

Tipos de datos básicos
---
- **Boolean**, (`bool`): El tipo de dato más básico, solo puede tomar los valores _`true`_ o _`false`_.
	- `let is_true: bool = true;`

- **Entero sin signo** (`u16, u32, u64`): Representa números naturales (_0, +∞_). El valor máximo que puede representar varía según el tamaño de bits adjudicado (8, 16, 32, etc.).
	-  `let u: u32 = 3;`

- **Entero con signo** (`i16, i32, i64`):  Representa números enteros (_-∞, +∞_). Sus valores mínimos y máximos varían según el tamaño de bits adjudicado (8, 16, 32, etc.).
	- `let i: i32 = 2;`
	- `let i: i32 = -3;` 

- **Flotante** (`f32, f64`): Representa números racionales. Sus valores mínimos y máximos varían según el tamaño de bits adjudicado (32 o 64).
	- `let f: i32 = 2.0;`
	- `let f: i32 = -3.0;`

- **Carácter** (`char`): Representa un carácter individual, declarado entre comillas simples.
	- `let c: char = 'C';`

- **Cadena (propietaria)** (`String`): Representa cadenas de caracteres y permite operaciones más complejas. Debe declararse explícitamente como un tipo `String`.
	- `let s: String = String::new(); // String vacio`
	- `let s: String = String::from("Hola que tal estas?");`

- **Referencia a cadena** (`&str`): Representa una visualización de una cadena de caracteres que toma prestado su valor. No es propietaria de la cadena.
	- `let s: &str = "Hola que tal estas?";`

- **Arrays** (`[u32, 4]`): Los arrays almacenan multiples valores de un mismo tipo en una coleccion que no puede cambiar de tamaño. Son de tipo y tamaño fijo.
	- `let array: [i32; 4] = [1, 2, 3, 4];`

- **Tuplas** (`(u32, i16, char, f64)`): Las tuplas permiten agrupar valores de distinto tipo en una coleccion que no puede cambiar de tamaño. Son de tamaño fijo pero tipo variable.
	- `let tupla: (u32, i16, char, f64) = (2, -3, 'c', 5.6);`

- **Vectores** (`Vec<i32>`): Los vectores permiten almacenar valores de un mismo tipo en una coleccion y ademas pueden cambiar de tamaño. Son de tamaño variable y tipo fijo.
	- `let mut vector: Vec<i32> = Vec::new();`

En Rust se puede declarar multiples variables que posean el mismo nombre, siempre y cuando estas variables no tengan el mismo tipo de dato.

Shadowing
---
El shadowing es una caracteristica que permite la declarar una nueva variable que posea el nombre de otra variable dentro del mismo scope. Esto nos permite reasignar valores a variables, incluso a aquellas que originalmente no habian sido declaradas con `mut`.

Ejemplo de shadowing basico:
```rust
let x: u32 = 5; // x = 5
let x: u32 = x + 1; // x = 5 + 1
let x: u32 = x * 2; //  x = 6 * 2
    
println!("El valor de x es: {}", x); // Salida: 12
```
Utilizando shadowing podemos llegar a cambiar el tipado de una variable.

Ejemplo de cambio de tipo de una variable:
```rust
let var: String = String::from("123"); // var = "123"
let var = var.len(); // var = 3
    
println!("{}", var); // Salida: 3
``` 

Condicionales
---
En Rust, las condiciones se especifican con las palabras clave `if`, `else` y `else if`.
Si quieres trabajar con múltiples condiciones , puedes usar operadores lógicos como `&&`, `||` y `!` para combinar condiciones.

Ejemplo básico:
```rust
let age: u32 = 24;
if age < 18 {
	println!("Menor de edad.");
}else if age == 18 {
	println!("Acaba de cumplir 18.");
}else {
	println!("Mayor de edad.");
} // Salida: Mayor de edad.
```

Ejemplo con operador ternario:
```rust
let age: u32 = 24;
let can_vote: bool = if age <= 18 {false} else {true}; 
    
println!("{}", can_vote) // Salida: true
```

Además de las palabras clave `if`, `else if` y `else`, Rust proporciona la palabra clave `match` para la comparación de patrones. Tiene una funcionalidad similar al `switch` en otros lenguajes como Java o C, pero con una sintaxis más poderosa y flexible.

Ejemplo con match:
```rust
let number: u32 = 7;
    
match number {
	1 => println!("Es el numero 1."),
	3 | 5 | 7 | 11 => println!("Es un numero primo."),
	_ => println!("Es otro numero cualquiera."),
}	// Salida es un numero primo.
```

Bucles
---
En rust existen 3 tipos de bucles principales el `loop` el `while` y `for`.

- **Loop**: Mantendra el bucle activo hasta que encuentre la palabra clave `break`.
	```rust
	let mut number: u32 = 0;
	    
	loop {
		println!("Inside loop.");
		number += 1; 
		if number == 5 {break};
	}
	``` 

- **While**: Mantendra el bucle activo hasta que se cumpla la condicion de su declaracion.
	```rust
	let mut number: u32 = 0;
	    
	while number < 5 {
		println!("Inside loop.");
		number += 1;
	}
	```
- **For**: Mantendra el bucle mientras recorre algun tipo de iterador. Puede seleccionar el elemento del iterador que esta recorriendo en este momento como una variable.
	```rust
	for _ in 0..5 {
		println!("Inside loop.")
	} // Salida: Inside loop * 5
	    
	for x in 0..5 {
	println!("{}", x)
	} // Salida: 0, 1, 2, 3, 4
	    
	for x in (0..10).step_by(2) {
		println!("{}", x)
	} // Salida: 0, 2, 4, 6, 8
	    
	let array: [u32; 5] = [1, 2, 3, 4, 5];
	for x in array.iter() {
		println!("{}", x)
	} // Salida: 1, 2, 3, 4, 5
	```
