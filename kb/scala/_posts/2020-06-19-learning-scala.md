---
layout: post
title: "Notes from learning Scala"
date: 2020-06-19
---

## List of resources
* Programming in Scala, Third Edition
* Functional Programming in Scala

## Introduction
* `val` vs. `var`
* type inference
* primitive Java types are used where possible for performance
* arguments are passed in `args` array
* ! scala 2.13.2 not working with urxvt - bug in JLine? should be fixed, but not in current version, using xfce4-term for now
* recommended indentation style: two spaces
* `i++` and `++i` are not valid, must increment with `i += 1`
* `f(arg)` gets transformed into `f.apply(arg)` - e.g. accessing array value is a method call to `apply`
  * all operations in Scala are method calls
  * assignment = `update` method call (`array(0) = "string" == array.update(0, "string")`)
* array initialization `val x = Array("one", "two")`
* List: `val x = List(1, 2)`
  * cons `::`, concatenation `:::`
* Array is mutable, List is immutable
* if a method name ends with colon (e.g. `::`), it is invoked on the right operand, otherwise on the left one
  * `1 :: x == x.::(1)`
* empty List = `Nil` or `List()`
* useful List methods: `drop, dropRight, count, exists, filter, forAll, length, isEmpty, mkString, reverse, sort`
* tuples 
  * accessing elements through `._1, ._2,...`
* sets
  * there are both mutable and immutable (default) variants
* maps
  * mutable and immutable variants as well

## Classes and Objects
* class members (fields and methods) are public by default
* `procedure` = method called only for it´s side-effect
* classes can´t have static members - Scala has singleton objects instead
  * keyword `object`
  * if `class` and `object` have the same name, the object is called the `companion object`
    * companion class and object have to be defined in the same file
  * singleton objects can´t be parameterized, unlike classes (s. objects can´t be instantiated with a `new` keyword)
* `standalone object` - when the object´s name does not match a class name (useful for e.g. encapsulating related methods)
* application entry point
  * any standalone singleton object with a proper signature (type Unit, args parameter)
* App trait - eliminates need to define main method, automatically exposes args

## Basic Types and Operations
* *string interpolators*: `s`, `raw`, `f`
* all methods can be used in operator notation (e.g. `"hello" contains "o"` or `7 toLong`)
* only `+, -, !, ~` can be used as prefix operators
* convention on using parentheses when invoking methods: if method has side effects, include them (`println()`), otherwise they are not needed (`"Hello".toLowerCase`)
* logical operators: `||, &&` - short-circuit (from left; right side may not be evaluated)
  * non-short-circuiting variants: `|, &`
* bitwise operations: or `|`, and `&`, xor `^`, complement `~`
  * shift left `<<`, shift right `>>`, unsigned shift right `>>>`
* `==`, `!=` - *value equality* (on objects, unlike Java´s *reference equality*)
* operator precedence - based on the first character (e.g. `* /` has higher precedence than `+ -` and therefore `***` > `+++`)
  * *assignment operators* (end with `=` symbol) - lowest precedence
  * operands are always evaluated from the left (no matter the operator associativity)
    * in `a ::: b`, `a` is evaluated first, even though `:::` method is invoked on `b` with `a` as an argument

## Functional Objects
* class parameters are only accessible from the current object
  * define fields, if you need to access the other objects parameters (e.g. adding Rational numbers)
* self-reference - `this` keyword
* *auxiliary constructors* - other than the primary constructor (`def this...`)
  * must call other class constructor (auxiliary or primary)
  * ultimately, each constructor will call the primary class constructor (even if transitively)
* operators can be used in method names
* *identifiers*
  * *operator identifiers* - e.g. `+, ++, :->`
  * alphanumeric (camel case, avoid `_, $`)
    * constants in camel case as well, not upper case as in Java
  * *mixed identifiers* - of form `<alphanumeric>_<operator>`, e.g. `unary_+`
  * *literal identifier* - arbitrary string in backticks ``(`yield`)``

## Built-in Control Structures
* `if, while, try, match, for` and function calls
* `while` and `do-while` - try to avoid, as their return type is Unit; they likely modify vars or perform IO
* *for-expressions* - iterating through collections
  * works with ranges `for (i <- 1 to 4)`
  * nested iteration - multiple `x <- ...` expressions
  * mid-stream assignment (with `=` sign, creates a val)
  * producing a new collection - `for clauses yield body`
* try-catch-finally (finally should be used mainly for side-effects, e.g. cleanup, closing the file; should not return a value)
* match-case pattern matching
* possible to shadow variable name in an inner scope (although it may be confusing to readers)
* case class can be instantiated without using `new`

## Functions and Closures
* helper functions - make them private or nest inside functions (usually not necessary to be called by function clients)
* underscore as parameter placeholder `someNumbers.filter(_ > 0)`
  * equivalent to `someNumbers.filter(x => x > 0)` (as long as each parameter figures only once)
  * when using multiple undescores, the first one stands for the first parameter, second for second etc. `_ + _`
* partially applied functions
* closures
* special function call forms
  * repeated parameters (asterisk): `def echo(args: String*)`
  * named parameters - they need to come *after* positional parameters
  * default parameter values
* tail recursion optimization
  * only for self-referencing function (no optimization possible if the recursion is indirect)
  * tail recursive function are essentially compiled to while loops, having no performance penalty

## Intro (FPiS)
* Scala REPL - `:paste` to insert multiline block
* `@annotation.tailrec` to have the compiler check that all recursive function calls are tail-recursive (and do not use up unnecessary stack frames, leading to potential stack overflow)
* `compose, andThen` - part of Scala library

## Control Abstraction
* *loan pattern* - some resource (e.g. file) is loaned to a client, which does not need to worry about correctly closing it/clean up
* if a function takes a single argument, curly braces can be used instead of parentheses
  * useful in conjuction with currying `withFile(file: File, op: PrintWriter => Unit)` can be rewritten as `withFile(file: File)(op: PrintWriter => Unit)` and used as `withFile(file) {writer => ...}`
* *by-name parameters* - not sure about where to use them

## Composition and Inheritance
* *combinators* - composing operators
* method with no implementation - *abstract class member* (opposite of *concrete*)
  * class with abstract members must itself be declared abstract
  * abstract class can not be instantiated
* *parameterless* vs. *empty-paren* methods
  * Scala is liberal, more of a convention - parameterless methods should be used when there are no side-effects
* member of the subclass *overrides* (or *implements* in case of abstract superclass)  member of the superclass with the same name
* *subtyping* - value of the subclass can be used where a value of the superclass is required
* Scala has only 2 namespaces (for values and types)
  * method/field can override field/method with the same name
  * class can not contain field and method with the same name - they share the value namespace
* *parametric field* - defines parameter and the field of the same name (reduces duplication)
* *final* modifier
  * on class member -> can not be overriden
  * on class -> can not be subclassed
* *factory* - have a unified way how clients can create objects, regardless of implementation details (e.g. by having multiple overloaded constructors)
* *private classes* - to hide implementation details

## Scala´s Hierarchy
* *Any* - common superclass (every class inherits from it), *Nothing* - common subclass (subclass of every other class)
* subclasses of *Any*: *AnyVal* (value classes, e.g. Int, Char), *AnyRef* (reference classes, equivalent to Java Object, e.g. List, Iterable,...)
* *eq* checks reference equality (`==` and `equals` check value equality - more consistent than Java)

## Traits
* *mix in* with `extends` or `with` keywords
* multiple traits can be mixed in `with Trait1 with Trait2`
* differences from classes:
  * can not take parameters (`trait T(x: Int)` is invalid)
  * `super` calls are dynamically bound
* *Ordered* trait
* possible use: stackable modifications
* order of traits is important - in general, the ones on the right take effect first (*linearization*)

## Packages and Imports
* intention: minimize coupling, increase modularity
* *_root_* package at the top of hierarchy
* imports can be renamed `import pkg.{Sql => S}`
* specific package members can be hidden `import pkg.{Hidden => _, _}` (imports everything except Hidden)
* *implicit imports*
  * packages imported to every source file: java.lang.\_, scala.\_, Predef.\_
* *access modifiers*: `private, protected`
  * can be enhanced with modifiers `private[X]`, meaning *private up to X* (X being some enclosing, higher-level package)
  * *object-private* access: `private[this]` -> visibility limited to the same instance (other objects of the same class can not access it)
* *package object* - visible everywhere in package

## Assertions and Tests
* `assert`, `ensuring`
* asserts are enabled with JVM parameter `-ea`
* ScalaTest, ScalaCheck

## Case Classes and Pattern Matching
* pattern types: *constant*, *constructor*, *variable*, *sequence* (for e.g. List), *tuple*, *typed*
* *type erasure* - no information about type arguments is maintained at runtime? (with the exception of Array)
* *variable binding* `case p @ List(1, _) => p`
* *pattern guards*
* *sealed* classes / traits - contained in one file -> safer for pattern matching
* `@unchecked` annotation - warning that pattern match is not exhaustive will be suppressed
* *Option* type
* patterns can be used in variable definitions (ex. of multiple assignment: `val (x, y) = (5, 6)`)

## Working with Lists
* concatenation `:::` (`++` works with all collections)
* `???` method - placeholder, throws `NotImplemented` exceptions
* `length` method - time proportional to number of elements => for checking emptiness, use `list.isEmpty` instead of `list.length == 0`
* other useful first-order methods: `drop`, `take`, `splitAt`, `reverse`, `indices`, `flatten`, `toString`, `mkString`
* `zip`, `unzip`, `zipWithIndex`
* higher-order methods: `map`, `flatMap`, `forEach`, `filter`, `partition`, `find`, `takeWhile`, `dropWhile`, `span`, `forAll`, `exists`, `foldLeft` (`/:`), `foldRight` (`:\`), `sortWith`
* methods of the List (companion) object: `List.range`, `List.fill`, `List.tabulate`, `List.concat`
* when designing a polymorphic method that takes a function and non-function arguments, place the function argument last in a curried parameter list of its own
  * better for type inference - Scala will infer the type from the first argument; if the function went first, its type could not be automatically inferred and would need to be explicitly specified

## Working With Other Collections
* `Sequence` - ordered collections
  * `List`, `Array`
  * `ListBuffer` - constant time append and prepend
  * `ArrayBuffer`, `StringOps` (implicit conversion from `String`)
* sets, maps
  * immutable versions take up less space
  * sorted variants: trait `SortedSet`, `SortedMap`
  
## Mutable Objects

## Type Parameterization
* generic types have by default *nonvariant* (rigid) subtyping
  * i.e. `Queue[String]` is not usable in place where `Queue[AnyRef]` is required
  * *variance annotations* (`+`, `-`)
  * *covariant* (flexible) subtyping can be specified by plus sign: `trait Queue[+T] {...}`, *contravariant* by minus
* type can be required to be a supertype of another, e.g. `def enqueue[U >: T](x: U)...` - U is required to be a supertype of T

## Abstract Members
* *abstract* = not having full definition in class
* can apply to *vals*, *vars*, *methods* and *types*
* abstract vals differ from method parameters in evaluation order - parameters are evaluated *before* being passed to class constructor, implementations of abstract vals *after*
  * *pre-initialized fields*: use braces `new { val numerArg = 1 * x } with RationalTrait`
  * `lazy val` - evaluated exactly once, on first usage; suitable for functional style without side effects, where execution order does not matter much
* *abstract types* - can be specialized in subclasses `type SuitableFood <: Food`
* *nominal* (standard) vs. *structural* subtyping (via *refinement types*)
* *enumerations* `object Color extends Enumeration { val Red, Blue, Green = Value }`

## Implicit Conversions and Parameters
* rules:
  * only declarations prefixed with `implicit` are taken into account
  * declaration must be in scope as a single identifier (i.e. `convert`, not `package.convert`) or be declared in a companion object
  * only one implicit is inserted (no chaining)
  * implicits are not tried if the code type checks
* types:
  * conversion to another type (`val x: Double = 3` -> implicit conversion from Int to Double is in Predef)
  * receiver conversion (`obj.method`, when object `obj` does not have `method` -> try to convert `obj`)
  * implicit parameters - prefer specific or custom types to minimize unwanted implicits (e.g. use `Email` instead of `String`)
* `implicitly`
* context bounds `method[T : Ordering]`
* when multiple implicit conversions could apply, the most specific is chosen (in older Scala versions, none would be)

## Implementing Lists
* two efficient ways to build a `List`:
  * prepending to `List` with `::`
  * using `ListBuffer` (implementation uses mutable state; adding to the end is also efficient) and calling `toList` at the end

## For Expressions Revisited
* all `for` expressions with `yield` are transformed by compiler into a combination of `map`, `flatMap`, `withFilter`
* all `for` expressions without `yield` compile into `withFilter` and `foreach`
* general form: `for ( seq ) yield expr`, where *seq* can contain *generators, definitions and filters*

## Collections in Depth
* trait *Traversable* - top of hierarchy, has abstract method `foreach`
* trait *Iterable* - abstract method `iterator`
  * `grouped` - iterator returns next *n* elements instead of just 1
  ```
  > val xs = List(1, 2, 3, 4, 5)
  > val git = xs grouped 3
  > git.next()
  List(1, 2, 3)
  > git.next()
  List(4, 5)
  ```
  * `sliding` - returns sliding window (List(1, 2, 3), List(2, 3, 4),...)
* `Seq, Set, Map`