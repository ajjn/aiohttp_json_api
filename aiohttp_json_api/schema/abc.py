class FieldABC(object):
    def getter(self, f):
        raise NotImplementedError

    def setter(self, f):
        raise NotImplementedError

    def validator(self, f, step, on):
        raise NotImplementedError

    async def default_get(self, schema, resource, **kwargs):
        raise NotImplementedError

    async def default_set(self, schema, resource, data, sp, **kwargs):
        raise NotImplementedError

    async def get(self, schema, resource, **kwargs):
        raise NotImplementedError

    async def set(self, schema, resource, data, sp, **kwargs):
        raise NotImplementedError

    def encode(self, schema, data, **kwargs):
        raise NotImplementedError

    def decode(self, schema, data, sp, **kwargs):
        raise NotImplementedError

    def pre_validate(self, schema, data, sp, context):
        raise NotImplementedError

    def post_validate(self, schema, data, sp, context):
        raise NotImplementedError


class SchemaABC(object):
    #: The JSON API *type*. (Leave it empty to derive it automatic from the
    #: resource class name or the schema name).
    type = None
    resource_class = None
    opts = None
    inflect = None

    def get_relationship_field(self, relation_name, source_parameter=None):
        raise NotImplementedError

    async def encode_resource(self, resource, **kwargs):
        raise NotImplementedError

    def encode_relationship(self, relation_name, resource, *, pagination=None):
        raise NotImplementedError

    def validate_resource_pre_decode(self, data, sp, context, *,
                                     expected_id=None):
        raise NotImplementedError

    def decode_resource(self, data, sp):
        raise NotImplementedError

    def validate_resource_post_decode(self, memo, context):
        raise NotImplementedError

    async def create_resource(self, data, sp, context, **kwargs):
        raise NotImplementedError

    async def update_resource(self, resource, data, sp, context, **kwargs):
        raise NotImplementedError

    async def delete_resource(self, resource, context, **kwargs):
        raise NotImplementedError

    async def update_relationship(self, relation_name, resource,
                                  data, sp, context, **kwargs):
        raise NotImplementedError

    async def add_relationship(self, relation_name, resource,
                               data, sp, context, **kwargs):
        raise NotImplementedError

    async def remove_relationship(self, relation_name, resource,
                                  data, sp, context, **kwargs):
        raise NotImplementedError

    async def query_collection(self, context, **kwargs):
        raise NotImplementedError

    async def query_resource(self, resource_id, context, **kwargs):
        raise NotImplementedError

    async def query_relative(self, relation_name, resource, context, **kwargs):
        raise NotImplementedError

    async def query_relatives(self, relation_name, resource, context, **kwargs):
        raise NotImplementedError

    async def fetch_include(self, relation_name, resources, context, *,
                            rest_path=None, **kwargs):
        raise NotImplementedError