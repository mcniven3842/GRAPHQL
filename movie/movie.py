from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolvers as r

#The host and port implemented by the movie service are defined
PORT = 3001
HOST = '0.0.0.0'
app = Flask(__name__)
################################################
# the entry points are defined
################################################
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>", 200)

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods=['POST'])
def graphql_server():
# The types declared in the movie.graphql schema are loaded
    type_defs = load_schema_from_path('movie.graphql')
# Create the objects associated to the schema, there are 4 types of objects in this case:
#   movie, actor, query and mutation
    query = QueryType()
    mutation = MutationType()
    movie = ObjectType('Movie')
    actor = ObjectType('Actor')
#  The resolver is attached to the list of actors to be constructed in the schema movie type. To do this we use the set_field method as before, but this time for the movie object we have constructed.
#  The field to resolve in the schema is actors and we attach our resolver r.resolve_actors_in_movie to it. 
    movie.set_field('actors', r.resolve_actors_in_movie)
# Associates the resolver with the associated query in the schema.
    query.set_field('movie_with_id', r.movie_with_id)
    query.set_field('all_movies', r.all_movies)  
# Associates the resolver with the associated mutation in the schema.
    mutation.set_field('update_movie_rate', r.update_movie_rate)
    mutation.set_field('delete_movie', r.delete_movie)
    mutation.set_field('add_movie', r.add_movie)
    mutation.set_field('update_movie', r.update_movie)
#A schema called executable is created with the above elements.
    schema = make_executable_schema(type_defs, movie, query, mutation, actor)

    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
