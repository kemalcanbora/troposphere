# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class ApiDestination(AWSObject):
    """
    `ApiDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html>`__
    """

    resource_type = "AWS::Events::ApiDestination"

    props: PropsDictType = {
        "ConnectionArn": (str, True),
        "Description": (str, False),
        "HttpMethod": (str, True),
        "InvocationEndpoint": (str, True),
        "InvocationRateLimitPerSecond": (integer, False),
        "Name": (str, False),
    }


class Archive(AWSObject):
    """
    `Archive <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html>`__
    """

    resource_type = "AWS::Events::Archive"

    props: PropsDictType = {
        "ArchiveName": (str, False),
        "Description": (str, False),
        "EventPattern": (dict, False),
        "RetentionDays": (integer, False),
        "SourceArn": (str, True),
    }


class Connection(AWSObject):
    """
    `Connection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html>`__
    """

    resource_type = "AWS::Events::Connection"

    props: PropsDictType = {
        "AuthParameters": (dict, True),
        "AuthorizationType": (str, True),
        "Description": (str, False),
        "Name": (str, False),
    }


class EventBus(AWSObject):
    """
    `EventBus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html>`__
    """

    resource_type = "AWS::Events::EventBus"

    props: PropsDictType = {
        "EventSourceName": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Condition(AWSProperty):
    """
    `Condition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Type": (str, False),
        "Value": (str, False),
    }


class EventBusPolicy(AWSObject):
    """
    `EventBusPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html>`__
    """

    resource_type = "AWS::Events::EventBusPolicy"

    props: PropsDictType = {
        "Action": (str, False),
        "Condition": (Condition, False),
        "EventBusName": (str, False),
        "Principal": (str, False),
        "Statement": (dict, False),
        "StatementId": (str, True),
    }


class BatchArrayProperties(AWSProperty):
    """
    `BatchArrayProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batcharrayproperties.html>`__
    """

    props: PropsDictType = {
        "Size": (integer, False),
    }


class BatchRetryStrategy(AWSProperty):
    """
    `BatchRetryStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchretrystrategy.html>`__
    """

    props: PropsDictType = {
        "Attempts": (integer, False),
    }


class BatchParameters(AWSProperty):
    """
    `BatchParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html>`__
    """

    props: PropsDictType = {
        "ArrayProperties": (BatchArrayProperties, False),
        "JobDefinition": (str, True),
        "JobName": (str, True),
        "RetryStrategy": (BatchRetryStrategy, False),
    }


class DeadLetterConfig(AWSProperty):
    """
    `DeadLetterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-deadletterconfig.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    `CapacityProviderStrategyItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html>`__
    """

    props: PropsDictType = {
        "Base": (integer, False),
        "CapacityProvider": (str, True),
        "Weight": (integer, False),
    }


class AwsVpcConfiguration(AWSProperty):
    """
    `AwsVpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-awsvpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssignPublicIp": (str, False),
        "SecurityGroups": ([str], False),
        "Subnets": ([str], True),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "AwsVpcConfiguration": (AwsVpcConfiguration, False),
    }


class PlacementConstraint(AWSProperty):
    """
    `PlacementConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Type": (str, False),
    }


class PlacementStrategy(AWSProperty):
    """
    `PlacementStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html>`__
    """

    props: PropsDictType = {
        "Field": (str, False),
        "Type": (str, False),
    }


class EcsParameters(AWSProperty):
    """
    `EcsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html>`__
    """

    props: PropsDictType = {
        "CapacityProviderStrategy": ([CapacityProviderStrategyItem], False),
        "EnableECSManagedTags": (boolean, False),
        "EnableExecuteCommand": (boolean, False),
        "Group": (str, False),
        "LaunchType": (str, False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PlacementConstraints": ([PlacementConstraint], False),
        "PlacementStrategies": ([PlacementStrategy], False),
        "PlatformVersion": (str, False),
        "PropagateTags": (str, False),
        "ReferenceId": (str, False),
        "TagList": (Tags, False),
        "TaskCount": (integer, False),
        "TaskDefinitionArn": (str, True),
    }


class HttpParameters(AWSProperty):
    """
    `HttpParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html>`__
    """

    props: PropsDictType = {
        "HeaderParameters": (dict, False),
        "PathParameterValues": ([str], False),
        "QueryStringParameters": (dict, False),
    }


class InputTransformer(AWSProperty):
    """
    `InputTransformer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html>`__
    """

    props: PropsDictType = {
        "InputPathsMap": (dict, False),
        "InputTemplate": (str, True),
    }


class KinesisParameters(AWSProperty):
    """
    `KinesisParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html>`__
    """

    props: PropsDictType = {
        "PartitionKeyPath": (str, True),
    }


class RedshiftDataParameters(AWSProperty):
    """
    `RedshiftDataParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html>`__
    """

    props: PropsDictType = {
        "Database": (str, True),
        "DbUser": (str, False),
        "SecretManagerArn": (str, False),
        "Sql": (str, True),
        "StatementName": (str, False),
        "WithEvent": (boolean, False),
    }


class RetryPolicy(AWSProperty):
    """
    `RetryPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-retrypolicy.html>`__
    """

    props: PropsDictType = {
        "MaximumEventAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
    }


class RunCommandTarget(AWSProperty):
    """
    `RunCommandTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Values": ([str], True),
    }


class RunCommandParameters(AWSProperty):
    """
    `RunCommandParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html>`__
    """

    props: PropsDictType = {
        "RunCommandTargets": ([RunCommandTarget], True),
    }


class SageMakerPipelineParameter(AWSProperty):
    """
    `SageMakerPipelineParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class SageMakerPipelineParameters(AWSProperty):
    """
    `SageMakerPipelineParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameters.html>`__
    """

    props: PropsDictType = {
        "PipelineParameterList": ([SageMakerPipelineParameter], False),
    }


class SqsParameters(AWSProperty):
    """
    `SqsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html>`__
    """

    props: PropsDictType = {
        "MessageGroupId": (str, True),
    }


class Target(AWSProperty):
    """
    `Target <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "BatchParameters": (BatchParameters, False),
        "DeadLetterConfig": (DeadLetterConfig, False),
        "EcsParameters": (EcsParameters, False),
        "HttpParameters": (HttpParameters, False),
        "Id": (str, True),
        "Input": (str, False),
        "InputPath": (str, False),
        "InputTransformer": (InputTransformer, False),
        "KinesisParameters": (KinesisParameters, False),
        "RedshiftDataParameters": (RedshiftDataParameters, False),
        "RetryPolicy": (RetryPolicy, False),
        "RoleArn": (str, False),
        "RunCommandParameters": (RunCommandParameters, False),
        "SageMakerPipelineParameters": (SageMakerPipelineParameters, False),
        "SqsParameters": (SqsParameters, False),
    }


class Rule(AWSObject):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html>`__
    """

    resource_type = "AWS::Events::Rule"

    props: PropsDictType = {
        "Description": (str, False),
        "EventBusName": (str, False),
        "EventPattern": (dict, False),
        "Name": (str, False),
        "RoleArn": (str, False),
        "ScheduleExpression": (str, False),
        "State": (str, False),
        "Targets": ([Target], False),
    }
