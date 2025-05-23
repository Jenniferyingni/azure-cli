# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor action-group identity assign",
)
class Assign(AAZCommand):
    """Assign the user or system managed identities.

    :example: Add a system assigned managed identity to an existing action group.
        az monitor action-group identity assign --name ag --resource-group rg --system-assigned

    :example: Add a user assigned managed identity to an existing action group.
        az monitor action-group identity assign --name ag --resource-group rg --user-assigned MyAssignedId

    :example: Add system assigned identity and a user assigned managed identity to an existing action group.
        az monitor action-group identity assign --name ag --resource-group rg --system-assigned --user-assigned MyAssignedId
    """

    _aaz_info = {
        "version": "2024-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/actiongroups/{}", "2024-10-01-preview", "identity"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.action_group_name = AAZStrArg(
            options=["-n", "--name", "--action-group-name"],
            help="The name of the action group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ActionGroup.identity"

        _args_schema = cls._args_schema
        _args_schema.mi_system_assigned = AAZStrArg(
            options=["--system-assigned", "--mi-system-assigned"],
            arg_group="ActionGroup.identity",
            help="Set the system managed identity.",
            blank="True",
        )
        _args_schema.mi_user_assigned = AAZListArg(
            options=["--user-assigned", "--mi-user-assigned"],
            arg_group="ActionGroup.identity",
            help="Set the user managed identities.",
            blank=[],
        )

        mi_user_assigned = cls._args_schema.mi_user_assigned
        mi_user_assigned.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ActionGroupsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.selectors.subresource.required())
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.post_instance_update(self.ctx.selectors.subresource.required())
        self.ActionGroupsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            return result.identity

        def _set(self, value):
            result = self.ctx.vars.instance
            result.identity = value
            return

    class ActionGroupsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/actionGroups/{actionGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "actionGroupName", self.ctx.args.action_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _AssignHelper._build_schema_action_group_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class ActionGroupsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/actionGroups/{actionGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "actionGroupName", self.ctx.args.action_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _AssignHelper._build_schema_action_group_resource_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.selectors.subresource.required())

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZIdentityObjectType
            )
            _builder.set_prop("userAssigned", AAZListType, ".mi_user_assigned", typ_kwargs={"flags": {"action": "assign"}})
            _builder.set_prop("systemAssigned", AAZStrType, ".mi_system_assigned", typ_kwargs={"flags": {"action": "assign"}})

            user_assigned = _builder.get(".userAssigned")
            if user_assigned is not None:
                user_assigned.set_elements(AAZStrType, ".")

            return _instance_value


class _AssignHelper:
    """Helper class for Assign"""

    _schema_action_group_resource_read = None

    @classmethod
    def _build_schema_action_group_resource_read(cls, _schema):
        if cls._schema_action_group_resource_read is not None:
            _schema.id = cls._schema_action_group_resource_read.id
            _schema.identity = cls._schema_action_group_resource_read.identity
            _schema.location = cls._schema_action_group_resource_read.location
            _schema.name = cls._schema_action_group_resource_read.name
            _schema.properties = cls._schema_action_group_resource_read.properties
            _schema.tags = cls._schema_action_group_resource_read.tags
            _schema.type = cls._schema_action_group_resource_read.type
            return

        cls._schema_action_group_resource_read = _schema_action_group_resource_read = AAZObjectType()

        action_group_resource_read = _schema_action_group_resource_read
        action_group_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        action_group_resource_read.identity = AAZIdentityObjectType()
        action_group_resource_read.location = AAZStrType(
            flags={"required": True},
        )
        action_group_resource_read.name = AAZStrType(
            flags={"read_only": True},
        )
        action_group_resource_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        action_group_resource_read.tags = AAZDictType()
        action_group_resource_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_action_group_resource_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_action_group_resource_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType(
            nullable=True,
        )

        _element = _schema_action_group_resource_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_action_group_resource_read.properties
        properties.arm_role_receivers = AAZListType(
            serialized_name="armRoleReceivers",
        )
        properties.automation_runbook_receivers = AAZListType(
            serialized_name="automationRunbookReceivers",
        )
        properties.azure_app_push_receivers = AAZListType(
            serialized_name="azureAppPushReceivers",
        )
        properties.azure_function_receivers = AAZListType(
            serialized_name="azureFunctionReceivers",
        )
        properties.email_receivers = AAZListType(
            serialized_name="emailReceivers",
        )
        properties.enabled = AAZBoolType(
            flags={"required": True},
        )
        properties.event_hub_receivers = AAZListType(
            serialized_name="eventHubReceivers",
        )
        properties.group_short_name = AAZStrType(
            serialized_name="groupShortName",
            flags={"required": True},
        )
        properties.incident_receivers = AAZListType(
            serialized_name="incidentReceivers",
        )
        properties.itsm_receivers = AAZListType(
            serialized_name="itsmReceivers",
        )
        properties.logic_app_receivers = AAZListType(
            serialized_name="logicAppReceivers",
        )
        properties.sms_receivers = AAZListType(
            serialized_name="smsReceivers",
        )
        properties.voice_receivers = AAZListType(
            serialized_name="voiceReceivers",
        )
        properties.webhook_receivers = AAZListType(
            serialized_name="webhookReceivers",
        )

        arm_role_receivers = _schema_action_group_resource_read.properties.arm_role_receivers
        arm_role_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.arm_role_receivers.Element
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.role_id = AAZStrType(
            serialized_name="roleId",
            flags={"required": True},
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )

        automation_runbook_receivers = _schema_action_group_resource_read.properties.automation_runbook_receivers
        automation_runbook_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.automation_runbook_receivers.Element
        _element.automation_account_id = AAZStrType(
            serialized_name="automationAccountId",
            flags={"required": True},
        )
        _element.is_global_runbook = AAZBoolType(
            serialized_name="isGlobalRunbook",
            flags={"required": True},
        )
        _element.managed_identity = AAZStrType(
            serialized_name="managedIdentity",
        )
        _element.name = AAZStrType()
        _element.runbook_name = AAZStrType(
            serialized_name="runbookName",
            flags={"required": True},
        )
        _element.service_uri = AAZStrType(
            serialized_name="serviceUri",
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )
        _element.webhook_resource_id = AAZStrType(
            serialized_name="webhookResourceId",
            flags={"required": True},
        )

        azure_app_push_receivers = _schema_action_group_resource_read.properties.azure_app_push_receivers
        azure_app_push_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.azure_app_push_receivers.Element
        _element.email_address = AAZStrType(
            serialized_name="emailAddress",
            flags={"required": True},
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )

        azure_function_receivers = _schema_action_group_resource_read.properties.azure_function_receivers
        azure_function_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.azure_function_receivers.Element
        _element.function_app_resource_id = AAZStrType(
            serialized_name="functionAppResourceId",
            flags={"required": True},
        )
        _element.function_name = AAZStrType(
            serialized_name="functionName",
            flags={"required": True},
        )
        _element.http_trigger_url = AAZStrType(
            serialized_name="httpTriggerUrl",
            flags={"required": True},
        )
        _element.managed_identity = AAZStrType(
            serialized_name="managedIdentity",
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )

        email_receivers = _schema_action_group_resource_read.properties.email_receivers
        email_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.email_receivers.Element
        _element.email_address = AAZStrType(
            serialized_name="emailAddress",
            flags={"required": True},
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.status = AAZStrType(
            flags={"read_only": True},
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )

        event_hub_receivers = _schema_action_group_resource_read.properties.event_hub_receivers
        event_hub_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.event_hub_receivers.Element
        _element.event_hub_name = AAZStrType(
            serialized_name="eventHubName",
            flags={"required": True},
        )
        _element.event_hub_name_space = AAZStrType(
            serialized_name="eventHubNameSpace",
            flags={"required": True},
        )
        _element.managed_identity = AAZStrType(
            serialized_name="managedIdentity",
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
            flags={"required": True},
        )
        _element.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )

        incident_receivers = _schema_action_group_resource_read.properties.incident_receivers
        incident_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.incident_receivers.Element
        _element.connection = AAZObjectType(
            flags={"required": True},
        )
        _element.incident_management_service = AAZStrType(
            serialized_name="incidentManagementService",
            flags={"required": True},
        )
        _element.mappings = AAZDictType(
            flags={"required": True},
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )

        connection = _schema_action_group_resource_read.properties.incident_receivers.Element.connection
        connection.id = AAZStrType(
            flags={"required": True},
        )
        connection.name = AAZStrType(
            flags={"required": True},
        )

        mappings = _schema_action_group_resource_read.properties.incident_receivers.Element.mappings
        mappings.Element = AAZStrType()

        itsm_receivers = _schema_action_group_resource_read.properties.itsm_receivers
        itsm_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.itsm_receivers.Element
        _element.connection_id = AAZStrType(
            serialized_name="connectionId",
            flags={"required": True},
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.region = AAZStrType(
            flags={"required": True},
        )
        _element.ticket_configuration = AAZStrType(
            serialized_name="ticketConfiguration",
            flags={"required": True},
        )
        _element.workspace_id = AAZStrType(
            serialized_name="workspaceId",
            flags={"required": True},
        )

        logic_app_receivers = _schema_action_group_resource_read.properties.logic_app_receivers
        logic_app_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.logic_app_receivers.Element
        _element.callback_url = AAZStrType(
            serialized_name="callbackUrl",
            flags={"required": True},
        )
        _element.managed_identity = AAZStrType(
            serialized_name="managedIdentity",
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"required": True},
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )

        sms_receivers = _schema_action_group_resource_read.properties.sms_receivers
        sms_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.sms_receivers.Element
        _element.country_code = AAZStrType(
            serialized_name="countryCode",
            flags={"required": True},
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.phone_number = AAZStrType(
            serialized_name="phoneNumber",
            flags={"required": True},
        )
        _element.status = AAZStrType(
            flags={"read_only": True},
        )

        voice_receivers = _schema_action_group_resource_read.properties.voice_receivers
        voice_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.voice_receivers.Element
        _element.country_code = AAZStrType(
            serialized_name="countryCode",
            flags={"required": True},
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.phone_number = AAZStrType(
            serialized_name="phoneNumber",
            flags={"required": True},
        )

        webhook_receivers = _schema_action_group_resource_read.properties.webhook_receivers
        webhook_receivers.Element = AAZObjectType()

        _element = _schema_action_group_resource_read.properties.webhook_receivers.Element
        _element.identifier_uri = AAZStrType(
            serialized_name="identifierUri",
        )
        _element.managed_identity = AAZStrType(
            serialized_name="managedIdentity",
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.object_id = AAZStrType(
            serialized_name="objectId",
        )
        _element.service_uri = AAZStrType(
            serialized_name="serviceUri",
            flags={"required": True},
        )
        _element.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )
        _element.use_aad_auth = AAZBoolType(
            serialized_name="useAadAuth",
        )
        _element.use_common_alert_schema = AAZBoolType(
            serialized_name="useCommonAlertSchema",
        )

        tags = _schema_action_group_resource_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_action_group_resource_read.id
        _schema.identity = cls._schema_action_group_resource_read.identity
        _schema.location = cls._schema_action_group_resource_read.location
        _schema.name = cls._schema_action_group_resource_read.name
        _schema.properties = cls._schema_action_group_resource_read.properties
        _schema.tags = cls._schema_action_group_resource_read.tags
        _schema.type = cls._schema_action_group_resource_read.type


__all__ = ["Assign"]
