# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.dms import CDC  # noqa: F401
from .validators.dms import FULL_LOAD  # noqa: F401
from .validators.dms import FULL_LOAD_AND_CDC  # noqa: F401
from .validators.dms import validate_network_port


class Certificate(AWSObject):
    """
    `Certificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html>`__
    """

    resource_type = "AWS::DMS::Certificate"

    props: PropsDictType = {
        "CertificateIdentifier": (str, False),
        "CertificatePem": (str, False),
        "CertificateWallet": (str, False),
    }


class DocDbSettings(AWSProperty):
    """
    `DocDbSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class DynamoDbSettings(AWSProperty):
    """
    `DynamoDbSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html>`__
    """

    props: PropsDictType = {
        "ServiceAccessRoleArn": (str, False),
    }


class ElasticsearchSettings(AWSProperty):
    """
    `ElasticsearchSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html>`__
    """

    props: PropsDictType = {
        "EndpointUri": (str, False),
        "ErrorRetryDuration": (integer, False),
        "FullLoadErrorPercentage": (integer, False),
        "ServiceAccessRoleArn": (str, False),
    }


class GcpMySQLSettings(AWSProperty):
    """
    `GcpMySQLSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html>`__
    """

    props: PropsDictType = {
        "AfterConnectScript": (str, False),
        "CleanSourceMetadataOnMismatch": (boolean, False),
        "DatabaseName": (str, False),
        "EventsPollInterval": (integer, False),
        "MaxFileSize": (integer, False),
        "ParallelLoadThreads": (integer, False),
        "Password": (str, False),
        "Port": (integer, False),
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
        "ServerName": (str, False),
        "ServerTimezone": (str, False),
        "Username": (str, False),
    }


class IbmDb2Settings(AWSProperty):
    """
    `IbmDb2Settings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class KafkaSettings(AWSProperty):
    """
    `KafkaSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html>`__
    """

    props: PropsDictType = {
        "Broker": (str, False),
        "IncludeControlDetails": (boolean, False),
        "IncludeNullAndEmpty": (boolean, False),
        "IncludeTableAlterOperations": (boolean, False),
        "IncludeTransactionDetails": (boolean, False),
        "NoHexPrefix": (boolean, False),
        "PartitionIncludeSchemaTable": (boolean, False),
        "SaslPassword": (str, False),
        "SaslUserName": (str, False),
        "SecurityProtocol": (str, False),
        "SslCaCertificateArn": (str, False),
        "SslClientCertificateArn": (str, False),
        "SslClientKeyArn": (str, False),
        "SslClientKeyPassword": (str, False),
        "Topic": (str, False),
    }


class KinesisSettings(AWSProperty):
    """
    `KinesisSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html>`__
    """

    props: PropsDictType = {
        "IncludeControlDetails": (boolean, False),
        "IncludeNullAndEmpty": (boolean, False),
        "IncludeTableAlterOperations": (boolean, False),
        "IncludeTransactionDetails": (boolean, False),
        "MessageFormat": (str, False),
        "NoHexPrefix": (boolean, False),
        "PartitionIncludeSchemaTable": (boolean, False),
        "ServiceAccessRoleArn": (str, False),
        "StreamArn": (str, False),
    }


class MicrosoftSqlServerSettings(AWSProperty):
    """
    `MicrosoftSqlServerSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class MongoDbSettings(AWSProperty):
    """
    `MongoDbSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html>`__
    """

    props: PropsDictType = {
        "AuthMechanism": (str, False),
        "AuthSource": (str, False),
        "AuthType": (str, False),
        "DatabaseName": (str, False),
        "DocsToInvestigate": (str, False),
        "ExtractDocId": (str, False),
        "NestingLevel": (str, False),
        "Password": (str, False),
        "Port": (validate_network_port, False),
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
        "ServerName": (str, False),
        "Username": (str, False),
    }


class MySqlSettings(AWSProperty):
    """
    `MySqlSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class NeptuneSettings(AWSProperty):
    """
    `NeptuneSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html>`__
    """

    props: PropsDictType = {
        "ErrorRetryDuration": (integer, False),
        "IamAuthEnabled": (boolean, False),
        "MaxFileSize": (integer, False),
        "MaxRetryCount": (integer, False),
        "S3BucketFolder": (str, False),
        "S3BucketName": (str, False),
        "ServiceAccessRoleArn": (str, False),
    }


class OracleSettings(AWSProperty):
    """
    `OracleSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerOracleAsmAccessRoleArn": (str, False),
        "SecretsManagerOracleAsmSecretId": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class PostgreSqlSettings(AWSProperty):
    """
    `PostgreSqlSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class RedisSettings(AWSProperty):
    """
    `RedisSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html>`__
    """

    props: PropsDictType = {
        "AuthPassword": (str, False),
        "AuthType": (str, False),
        "AuthUserName": (str, False),
        "Port": (validate_network_port, False),
        "ServerName": (str, False),
        "SslCaCertificateArn": (str, False),
        "SslSecurityProtocol": (str, False),
    }


class RedshiftSettings(AWSProperty):
    """
    `RedshiftSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class S3Settings(AWSProperty):
    """
    `S3Settings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html>`__
    """

    props: PropsDictType = {
        "AddColumnName": (boolean, False),
        "BucketFolder": (str, False),
        "BucketName": (str, False),
        "CannedAclForObjects": (str, False),
        "CdcInsertsAndUpdates": (boolean, False),
        "CdcInsertsOnly": (boolean, False),
        "CdcMaxBatchInterval": (integer, False),
        "CdcMinFileSize": (integer, False),
        "CdcPath": (str, False),
        "CompressionType": (str, False),
        "CsvDelimiter": (str, False),
        "CsvNoSupValue": (str, False),
        "CsvNullValue": (str, False),
        "CsvRowDelimiter": (str, False),
        "DataFormat": (str, False),
        "DataPageSize": (integer, False),
        "DatePartitionDelimiter": (str, False),
        "DatePartitionEnabled": (boolean, False),
        "DatePartitionSequence": (str, False),
        "DatePartitionTimezone": (str, False),
        "DictPageSizeLimit": (integer, False),
        "EnableStatistics": (boolean, False),
        "EncodingType": (str, False),
        "EncryptionMode": (str, False),
        "ExternalTableDefinition": (str, False),
        "IgnoreHeaderRows": (integer, False),
        "IncludeOpForFullLoad": (boolean, False),
        "MaxFileSize": (integer, False),
        "ParquetTimestampInMillisecond": (boolean, False),
        "ParquetVersion": (str, False),
        "PreserveTransactions": (boolean, False),
        "Rfc4180": (boolean, False),
        "RowGroupLength": (integer, False),
        "ServerSideEncryptionKmsKeyId": (str, False),
        "ServiceAccessRoleArn": (str, False),
        "TimestampColumnName": (str, False),
        "UseCsvNoSupValue": (boolean, False),
        "UseTaskStartTimeForFullLoadTimestamp": (boolean, False),
    }


class SybaseSettings(AWSProperty):
    """
    `SybaseSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html>`__
    """

    props: PropsDictType = {
        "SecretsManagerAccessRoleArn": (str, False),
        "SecretsManagerSecretId": (str, False),
    }


class Endpoint(AWSObject):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html>`__
    """

    resource_type = "AWS::DMS::Endpoint"

    props: PropsDictType = {
        "CertificateArn": (str, False),
        "DatabaseName": (str, False),
        "DocDbSettings": (DocDbSettings, False),
        "DynamoDbSettings": (DynamoDbSettings, False),
        "ElasticsearchSettings": (ElasticsearchSettings, False),
        "EndpointIdentifier": (str, False),
        "EndpointType": (str, True),
        "EngineName": (str, True),
        "ExtraConnectionAttributes": (str, False),
        "GcpMySQLSettings": (GcpMySQLSettings, False),
        "IbmDb2Settings": (IbmDb2Settings, False),
        "KafkaSettings": (KafkaSettings, False),
        "KinesisSettings": (KinesisSettings, False),
        "KmsKeyId": (str, False),
        "MicrosoftSqlServerSettings": (MicrosoftSqlServerSettings, False),
        "MongoDbSettings": (MongoDbSettings, False),
        "MySqlSettings": (MySqlSettings, False),
        "NeptuneSettings": (NeptuneSettings, False),
        "OracleSettings": (OracleSettings, False),
        "Password": (str, False),
        "Port": (validate_network_port, False),
        "PostgreSqlSettings": (PostgreSqlSettings, False),
        "RedisSettings": (RedisSettings, False),
        "RedshiftSettings": (RedshiftSettings, False),
        "ResourceIdentifier": (str, False),
        "S3Settings": (S3Settings, False),
        "ServerName": (str, False),
        "SslMode": (str, False),
        "SybaseSettings": (SybaseSettings, False),
        "Tags": (Tags, False),
        "Username": (str, False),
    }


class EventSubscription(AWSObject):
    """
    `EventSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html>`__
    """

    resource_type = "AWS::DMS::EventSubscription"

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "EventCategories": ([str], False),
        "SnsTopicArn": (str, True),
        "SourceIds": ([str], False),
        "SourceType": (str, False),
        "SubscriptionName": (str, False),
        "Tags": (Tags, False),
    }


class ReplicationInstance(AWSObject):
    """
    `ReplicationInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html>`__
    """

    resource_type = "AWS::DMS::ReplicationInstance"

    props: PropsDictType = {
        "AllocatedStorage": (integer, False),
        "AllowMajorVersionUpgrade": (boolean, False),
        "AutoMinorVersionUpgrade": (boolean, False),
        "AvailabilityZone": (str, False),
        "EngineVersion": (str, False),
        "KmsKeyId": (str, False),
        "MultiAZ": (boolean, False),
        "PreferredMaintenanceWindow": (str, False),
        "PubliclyAccessible": (boolean, False),
        "ReplicationInstanceClass": (str, True),
        "ReplicationInstanceIdentifier": (str, False),
        "ReplicationSubnetGroupIdentifier": (str, False),
        "ResourceIdentifier": (str, False),
        "Tags": (Tags, False),
        "VpcSecurityGroupIds": ([str], False),
    }


class ReplicationSubnetGroup(AWSObject):
    """
    `ReplicationSubnetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html>`__
    """

    resource_type = "AWS::DMS::ReplicationSubnetGroup"

    props: PropsDictType = {
        "ReplicationSubnetGroupDescription": (str, True),
        "ReplicationSubnetGroupIdentifier": (str, False),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
    }


class ReplicationTask(AWSObject):
    """
    `ReplicationTask <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html>`__
    """

    resource_type = "AWS::DMS::ReplicationTask"

    props: PropsDictType = {
        "CdcStartPosition": (str, False),
        "CdcStartTime": (double, False),
        "CdcStopPosition": (str, False),
        "MigrationType": (str, True),
        "ReplicationInstanceArn": (str, True),
        "ReplicationTaskIdentifier": (str, False),
        "ReplicationTaskSettings": (str, False),
        "ResourceIdentifier": (str, False),
        "SourceEndpointArn": (str, True),
        "TableMappings": (str, True),
        "Tags": (Tags, False),
        "TargetEndpointArn": (str, True),
        "TaskData": (str, False),
    }
