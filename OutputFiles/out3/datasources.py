class DataSource:

    def __init__(self,username,password,ipAddress,port,dataSchema,dataBaseType):
        self.username=username
        self.password=password
        self.ipAddress=ipAddress
        self.port=port
        self.dataSchema=dataSchema
        self.dataBaseType=dataBaseType
        self.connectionString=self.dataBaseType.value+"://"+self.username+":"+self.password+"@"+self.ipAddress+":"+self.port+"/"+self.dataSchema

    def getMySQLDataCourceConfig(self):
        datasource_config = {
            "name": "my_mysql_datasource",
            "class_name": "Datasource",
            "execution_engine": {
                "class_name": "SqlAlchemyExecutionEngine",
                "connection_string": self.connectionString,
            },
            "data_connectors": {
                "default_runtime_data_connector_name": {
                    "class_name": "RuntimeDataConnector",
                    "batch_identifiers": ["default_identifier_name"],
                },
                "default_inferred_data_connector_name": {
                    "class_name": "InferredAssetSqlDataConnector",
                    "include_schema_name": True,
                },
            },
        }
        return datasource_config