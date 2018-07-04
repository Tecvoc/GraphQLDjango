# GraphQLDjango

... Simple example to show the usage of graphql with django

queries
query {
  all: allCategories {
    name
  },
  ing: allIngredients {
    name,
    notes,
    category {
      name
    }
  }
}
