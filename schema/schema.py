from ariadne import make_executable_schema
from schema.query import query
from schema.mutation import mutation

type_defs = """
    type Query {
        users: [User!]!
        user(id: ID!): User
    }

    type Mutation {
        createUser(name: String!, age: Int!): User!
        deleteUser(id: ID!): Boolean!
    }

    type User {
        id: ID!
        name: String!
        age: Int!
    }
"""

schema = make_executable_schema(type_defs, query, mutation)
