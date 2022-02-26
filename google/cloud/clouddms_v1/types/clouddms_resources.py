# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.clouddms.v1",
    manifest={
        "DatabaseEngine",
        "DatabaseProvider",
        "SslConfig",
        "MySqlConnectionProfile",
        "PostgreSqlConnectionProfile",
        "CloudSqlConnectionProfile",
        "SqlAclEntry",
        "SqlIpConfig",
        "CloudSqlSettings",
        "StaticIpConnectivity",
        "ReverseSshConnectivity",
        "VpcPeeringConnectivity",
        "DatabaseType",
        "MigrationJob",
        "ConnectionProfile",
        "MigrationJobVerificationError",
    },
)


class DatabaseEngine(proto.Enum):
    r"""The database engine types."""
    DATABASE_ENGINE_UNSPECIFIED = 0
    MYSQL = 1
    POSTGRESQL = 2


class DatabaseProvider(proto.Enum):
    r"""The database providers."""
    DATABASE_PROVIDER_UNSPECIFIED = 0
    CLOUDSQL = 1
    RDS = 2


class SslConfig(proto.Message):
    r"""SSL configuration information.

    Attributes:
        type_ (google.cloud.clouddms_v1.types.SslConfig.SslType):
            Output only. The ssl config type according to 'client_key',
            'client_certificate' and 'ca_certificate'.
        client_key (str):
            Input only. The unencrypted PKCS#1 or PKCS#8 PEM-encoded
            private key associated with the Client Certificate. If this
            field is used then the 'client_certificate' field is
            mandatory.
        client_certificate (str):
            Input only. The x509 PEM-encoded certificate that will be
            used by the replica to authenticate against the source
            database server.If this field is used then the 'client_key'
            field is mandatory.
        ca_certificate (str):
            Required. Input only. The x509 PEM-encoded
            certificate of the CA that signed the source
            database server's certificate. The replica will
            use this certificate to verify it's connecting
            to the right host.
    """

    class SslType(proto.Enum):
        r"""Specifies The kind of ssl configuration used."""
        SSL_TYPE_UNSPECIFIED = 0
        SERVER_ONLY = 1
        SERVER_CLIENT = 2

    type_ = proto.Field(proto.ENUM, number=1, enum=SslType,)
    client_key = proto.Field(proto.STRING, number=2,)
    client_certificate = proto.Field(proto.STRING, number=3,)
    ca_certificate = proto.Field(proto.STRING, number=4,)


class MySqlConnectionProfile(proto.Message):
    r"""Specifies connection parameters required specifically for
    MySQL databases.

    Attributes:
        host (str):
            Required. The IP or hostname of the source
            MySQL database.
        port (int):
            Required. The network port of the source
            MySQL database.
        username (str):
            Required. The username that Database
            Migration Service will use to connect to the
            database. The value is encrypted when stored in
            Database Migration Service.
        password (str):
            Required. Input only. The password for the
            user that Database Migration Service will be
            using to connect to the database. This field is
            not returned on request, and the value is
            encrypted when stored in Database Migration
            Service.
        password_set (bool):
            Output only. Indicates If this connection
            profile password is stored.
        ssl (google.cloud.clouddms_v1.types.SslConfig):
            SSL configuration for the destination to
            connect to the source database.
        cloud_sql_id (str):
            If the source is a Cloud SQL database, use
            this field to provide the Cloud SQL instance ID
            of the source.
    """

    host = proto.Field(proto.STRING, number=1,)
    port = proto.Field(proto.INT32, number=2,)
    username = proto.Field(proto.STRING, number=3,)
    password = proto.Field(proto.STRING, number=4,)
    password_set = proto.Field(proto.BOOL, number=5,)
    ssl = proto.Field(proto.MESSAGE, number=6, message="SslConfig",)
    cloud_sql_id = proto.Field(proto.STRING, number=7,)


class PostgreSqlConnectionProfile(proto.Message):
    r"""Specifies connection parameters required specifically for
    PostgreSQL databases.

    Attributes:
        host (str):
            Required. The IP or hostname of the source
            PostgreSQL database.
        port (int):
            Required. The network port of the source
            PostgreSQL database.
        username (str):
            Required. The username that Database
            Migration Service will use to connect to the
            database. The value is encrypted when stored in
            Database Migration Service.
        password (str):
            Required. Input only. The password for the
            user that Database Migration Service will be
            using to connect to the database. This field is
            not returned on request, and the value is
            encrypted when stored in Database Migration
            Service.
        password_set (bool):
            Output only. Indicates If this connection
            profile password is stored.
        ssl (google.cloud.clouddms_v1.types.SslConfig):
            SSL configuration for the destination to
            connect to the source database.
        cloud_sql_id (str):
            If the source is a Cloud SQL database, use
            this field to provide the Cloud SQL instance ID
            of the source.
    """

    host = proto.Field(proto.STRING, number=1,)
    port = proto.Field(proto.INT32, number=2,)
    username = proto.Field(proto.STRING, number=3,)
    password = proto.Field(proto.STRING, number=4,)
    password_set = proto.Field(proto.BOOL, number=5,)
    ssl = proto.Field(proto.MESSAGE, number=6, message="SslConfig",)
    cloud_sql_id = proto.Field(proto.STRING, number=7,)


class CloudSqlConnectionProfile(proto.Message):
    r"""Specifies required connection parameters, and, optionally,
    the parameters required to create a Cloud SQL destination
    database instance.

    Attributes:
        cloud_sql_id (str):
            Output only. The Cloud SQL instance ID that
            this connection profile is associated with.
        settings (google.cloud.clouddms_v1.types.CloudSqlSettings):
            Immutable. Metadata used to create the
            destination Cloud SQL database.
        private_ip (str):
            Output only. The Cloud SQL database
            instance's private IP.
        public_ip (str):
            Output only. The Cloud SQL database
            instance's public IP.
    """

    cloud_sql_id = proto.Field(proto.STRING, number=1,)
    settings = proto.Field(proto.MESSAGE, number=2, message="CloudSqlSettings",)
    private_ip = proto.Field(proto.STRING, number=3,)
    public_ip = proto.Field(proto.STRING, number=4,)


class SqlAclEntry(proto.Message):
    r"""An entry for an Access Control list.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            The allowlisted value for the access control
            list.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when this access control entry expires in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example: ``2012-11-15T16:19:00.094Z``.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The time-to-leave of this access
            control entry.

            This field is a member of `oneof`_ ``expiration``.
        label (str):
            A label to identify this entry.
    """

    value = proto.Field(proto.STRING, number=1,)
    expire_time = proto.Field(
        proto.MESSAGE, number=10, oneof="expiration", message=timestamp_pb2.Timestamp,
    )
    ttl = proto.Field(
        proto.MESSAGE, number=11, oneof="expiration", message=duration_pb2.Duration,
    )
    label = proto.Field(proto.STRING, number=3,)


class SqlIpConfig(proto.Message):
    r"""IP Management configuration.

    Attributes:
        enable_ipv4 (google.protobuf.wrappers_pb2.BoolValue):
            Whether the instance should be assigned an
            IPv4 address or not.
        private_network (str):
            The resource link for the VPC network from which the Cloud
            SQL instance is accessible for private IP. For example,
            ``projects/myProject/global/networks/default``. This setting
            can be updated, but it cannot be removed after it is set.
        require_ssl (google.protobuf.wrappers_pb2.BoolValue):
            Whether SSL connections over IP should be
            enforced or not.
        authorized_networks (Sequence[google.cloud.clouddms_v1.types.SqlAclEntry]):
            The list of external networks that are allowed to connect to
            the instance using the IP. See
            https://en.wikipedia.org/wiki/CIDR_notation#CIDR_notation,
            also known as 'slash' notation (e.g. ``192.168.100.0/24``).
    """

    enable_ipv4 = proto.Field(proto.MESSAGE, number=1, message=wrappers_pb2.BoolValue,)
    private_network = proto.Field(proto.STRING, number=2,)
    require_ssl = proto.Field(proto.MESSAGE, number=3, message=wrappers_pb2.BoolValue,)
    authorized_networks = proto.RepeatedField(
        proto.MESSAGE, number=4, message="SqlAclEntry",
    )


class CloudSqlSettings(proto.Message):
    r"""Settings for creating a Cloud SQL database instance.

    Attributes:
        database_version (google.cloud.clouddms_v1.types.CloudSqlSettings.SqlDatabaseVersion):
            The database engine type and version.
        user_labels (Sequence[google.cloud.clouddms_v1.types.CloudSqlSettings.UserLabelsEntry]):
            The resource labels for a Cloud SQL instance to use to
            annotate any related underlying resources such as Compute
            Engine VMs. An object containing a list of "key": "value"
            pairs.

            Example:
            ``{ "name": "wrench", "mass": "18kg", "count": "3" }``.
        tier (str):
            The tier (or machine type) for this instance, for example:
            ``db-n1-standard-1`` (MySQL instances) or
            ``db-custom-1-3840`` (PostgreSQL instances). For more
            information, see `Cloud SQL Instance
            Settings <https://cloud.google.com/sql/docs/mysql/instance-settings>`__.
        storage_auto_resize_limit (google.protobuf.wrappers_pb2.Int64Value):
            The maximum size to which storage capacity
            can be automatically increased. The default
            value is 0, which specifies that there is no
            limit.
        activation_policy (google.cloud.clouddms_v1.types.CloudSqlSettings.SqlActivationPolicy):
            The activation policy specifies when the instance is
            activated; it is applicable only when the instance state is
            'RUNNABLE'. Valid values:

            'ALWAYS': The instance is on, and remains so even in the
            absence of connection requests.

            ``NEVER``: The instance is off; it is not activated, even if
            a connection request arrives.
        ip_config (google.cloud.clouddms_v1.types.SqlIpConfig):
            The settings for IP Management. This allows
            to enable or disable the instance IP and manage
            which external networks can connect to the
            instance. The IPv4 address cannot be disabled.
        auto_storage_increase (google.protobuf.wrappers_pb2.BoolValue):
            [default: ON] If you enable this setting, Cloud SQL checks
            your available storage every 30 seconds. If the available
            storage falls below a threshold size, Cloud SQL
            automatically adds additional storage capacity. If the
            available storage repeatedly falls below the threshold size,
            Cloud SQL continues to add storage until it reaches the
            maximum of 30 TB.
        database_flags (Sequence[google.cloud.clouddms_v1.types.CloudSqlSettings.DatabaseFlagsEntry]):
            The database flags passed to the Cloud SQL
            instance at startup. An object containing a list
            of "key": value pairs. Example: { "name":
            "wrench", "mass": "1.3kg", "count": "3" }.
        data_disk_type (google.cloud.clouddms_v1.types.CloudSqlSettings.SqlDataDiskType):
            The type of storage: ``PD_SSD`` (default) or ``PD_HDD``.
        data_disk_size_gb (google.protobuf.wrappers_pb2.Int64Value):
            The storage capacity available to the
            database, in GB. The minimum (and default) size
            is 10GB.
        zone (str):
            The Google Cloud Platform zone where your
            Cloud SQL datdabse instance is located.
        source_id (str):
            The Database Migration Service source connection profile ID,
            in the format:
            ``projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID``
        root_password (str):
            Input only. Initial root password.
        root_password_set (bool):
            Output only. Indicates If this connection
            profile root password is stored.
        collation (str):
            The Cloud SQL default instance level
            collation.
    """

    class SqlActivationPolicy(proto.Enum):
        r"""Specifies when the instance should be activated."""
        SQL_ACTIVATION_POLICY_UNSPECIFIED = 0
        ALWAYS = 1
        NEVER = 2

    class SqlDataDiskType(proto.Enum):
        r"""The storage options for Cloud SQL databases."""
        SQL_DATA_DISK_TYPE_UNSPECIFIED = 0
        PD_SSD = 1
        PD_HDD = 2

    class SqlDatabaseVersion(proto.Enum):
        r"""The database engine type and version."""
        SQL_DATABASE_VERSION_UNSPECIFIED = 0
        MYSQL_5_6 = 1
        MYSQL_5_7 = 2
        POSTGRES_9_6 = 3
        POSTGRES_11 = 4
        POSTGRES_10 = 5
        MYSQL_8_0 = 6
        POSTGRES_12 = 7
        POSTGRES_13 = 8

    database_version = proto.Field(proto.ENUM, number=1, enum=SqlDatabaseVersion,)
    user_labels = proto.MapField(proto.STRING, proto.STRING, number=2,)
    tier = proto.Field(proto.STRING, number=3,)
    storage_auto_resize_limit = proto.Field(
        proto.MESSAGE, number=4, message=wrappers_pb2.Int64Value,
    )
    activation_policy = proto.Field(proto.ENUM, number=5, enum=SqlActivationPolicy,)
    ip_config = proto.Field(proto.MESSAGE, number=6, message="SqlIpConfig",)
    auto_storage_increase = proto.Field(
        proto.MESSAGE, number=7, message=wrappers_pb2.BoolValue,
    )
    database_flags = proto.MapField(proto.STRING, proto.STRING, number=8,)
    data_disk_type = proto.Field(proto.ENUM, number=9, enum=SqlDataDiskType,)
    data_disk_size_gb = proto.Field(
        proto.MESSAGE, number=10, message=wrappers_pb2.Int64Value,
    )
    zone = proto.Field(proto.STRING, number=11,)
    source_id = proto.Field(proto.STRING, number=12,)
    root_password = proto.Field(proto.STRING, number=13,)
    root_password_set = proto.Field(proto.BOOL, number=14,)
    collation = proto.Field(proto.STRING, number=15,)


class StaticIpConnectivity(proto.Message):
    r"""The source database will allow incoming connections from the
    destination database's public IP. You can retrieve the Cloud SQL
    instance's public IP from the Cloud SQL console or using Cloud
    SQL APIs. No additional configuration is required.

    """


class ReverseSshConnectivity(proto.Message):
    r"""The details needed to configure a reverse SSH tunnel between
    the source and destination databases. These details will be used
    when calling the generateSshScript method (see
    https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateSshScript)
    to produce the script that will help set up the reverse SSH
    tunnel, and to set up the VPC peering between the Cloud SQL
    private network and the VPC.

    Attributes:
        vm_ip (str):
            Required. The IP of the virtual machine
            (Compute Engine) used as the bastion server for
            the SSH tunnel.
        vm_port (int):
            Required. The forwarding port of the virtual
            machine (Compute Engine) used as the bastion
            server for the SSH tunnel.
        vm (str):
            The name of the virtual machine (Compute
            Engine) used as the bastion server for the SSH
            tunnel.
        vpc (str):
            The name of the VPC to peer with the Cloud
            SQL private network.
    """

    vm_ip = proto.Field(proto.STRING, number=1,)
    vm_port = proto.Field(proto.INT32, number=2,)
    vm = proto.Field(proto.STRING, number=3,)
    vpc = proto.Field(proto.STRING, number=4,)


class VpcPeeringConnectivity(proto.Message):
    r"""The details of the VPC where the source database is located
    in Google Cloud. We will use this information to set up the VPC
    peering connection between Cloud SQL and this VPC.

    Attributes:
        vpc (str):
            The name of the VPC network to peer with the
            Cloud SQL private network.
    """

    vpc = proto.Field(proto.STRING, number=1,)


class DatabaseType(proto.Message):
    r"""A message defining the database engine and provider.

    Attributes:
        provider (google.cloud.clouddms_v1.types.DatabaseProvider):
            The database provider.
        engine (google.cloud.clouddms_v1.types.DatabaseEngine):
            The database engine.
    """

    provider = proto.Field(proto.ENUM, number=1, enum="DatabaseProvider",)
    engine = proto.Field(proto.ENUM, number=2, enum="DatabaseEngine",)


class MigrationJob(proto.Message):
    r"""Represents a Database Migration Service migration job object.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The name (URI) of this migration job
            resource, in the form of:
            projects/{project}/locations/{location}/instances/{instance}.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the migration
            job resource was created. A timestamp in RFC3339
            UTC "Zulu" format, accurate to nanoseconds.
            Example: "2014-10-02T15:01:23.045123456Z".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the migration
            job resource was last updated. A timestamp in
            RFC3339 UTC "Zulu" format, accurate to
            nanoseconds. Example:
            "2014-10-02T15:01:23.045123456Z".
        labels (Sequence[google.cloud.clouddms_v1.types.MigrationJob.LabelsEntry]):
            The resource labels for migration job to use to annotate any
            related underlying resources such as Compute Engine VMs. An
            object containing a list of "key": "value" pairs.

            Example:
            ``{ "name": "wrench", "mass": "1.3kg", "count": "3" }``.
        display_name (str):
            The migration job display name.
        state (google.cloud.clouddms_v1.types.MigrationJob.State):
            The current migration job state.
        phase (google.cloud.clouddms_v1.types.MigrationJob.Phase):
            Output only. The current migration job phase.
        type_ (google.cloud.clouddms_v1.types.MigrationJob.Type):
            Required. The migration job type.
        dump_path (str):
            The path to the dump file in Google Cloud Storage, in the
            format: (gs://[BUCKET_NAME]/[OBJECT_NAME]).
        source (str):
            Required. The resource name (URI) of the
            source connection profile.
        destination (str):
            Required. The resource name (URI) of the
            destination connection profile.
        reverse_ssh_connectivity (google.cloud.clouddms_v1.types.ReverseSshConnectivity):
            The details needed to communicate to the
            source over Reverse SSH tunnel connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        vpc_peering_connectivity (google.cloud.clouddms_v1.types.VpcPeeringConnectivity):
            The details of the VPC network that the
            source database is located in.

            This field is a member of `oneof`_ ``connectivity``.
        static_ip_connectivity (google.cloud.clouddms_v1.types.StaticIpConnectivity):
            static ip connectivity data (default, no
            additional details needed).

            This field is a member of `oneof`_ ``connectivity``.
        duration (google.protobuf.duration_pb2.Duration):
            Output only. The duration of the migration
            job (in seconds). A duration in seconds with up
            to nine fractional digits, terminated by 's'.
            Example: "3.5s".
        error (google.rpc.status_pb2.Status):
            Output only. The error details in case of
            state FAILED.
        source_database (google.cloud.clouddms_v1.types.DatabaseType):
            The database engine type and provider of the
            source.
        destination_database (google.cloud.clouddms_v1.types.DatabaseType):
            The database engine type and provider of the
            destination.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. If the migration job is
            completed, the time when it was completed.
    """

    class State(proto.Enum):
        r"""The current migration job states."""
        STATE_UNSPECIFIED = 0
        MAINTENANCE = 1
        DRAFT = 2
        CREATING = 3
        NOT_STARTED = 4
        RUNNING = 5
        FAILED = 6
        COMPLETED = 7
        DELETING = 8
        STOPPING = 9
        STOPPED = 10
        DELETED = 11
        UPDATING = 12
        STARTING = 13
        RESTARTING = 14
        RESUMING = 15

    class Phase(proto.Enum):
        r"""The current migration job phase."""
        PHASE_UNSPECIFIED = 0
        FULL_DUMP = 1
        CDC = 2
        PROMOTE_IN_PROGRESS = 3
        WAITING_FOR_SOURCE_WRITES_TO_STOP = 4
        PREPARING_THE_DUMP = 5

    class Type(proto.Enum):
        r"""The type of migration job (one-time or continuous)."""
        TYPE_UNSPECIFIED = 0
        ONE_TIME = 1
        CONTINUOUS = 2

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    display_name = proto.Field(proto.STRING, number=5,)
    state = proto.Field(proto.ENUM, number=6, enum=State,)
    phase = proto.Field(proto.ENUM, number=7, enum=Phase,)
    type_ = proto.Field(proto.ENUM, number=8, enum=Type,)
    dump_path = proto.Field(proto.STRING, number=9,)
    source = proto.Field(proto.STRING, number=10,)
    destination = proto.Field(proto.STRING, number=11,)
    reverse_ssh_connectivity = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="connectivity",
        message="ReverseSshConnectivity",
    )
    vpc_peering_connectivity = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="connectivity",
        message="VpcPeeringConnectivity",
    )
    static_ip_connectivity = proto.Field(
        proto.MESSAGE, number=103, oneof="connectivity", message="StaticIpConnectivity",
    )
    duration = proto.Field(proto.MESSAGE, number=12, message=duration_pb2.Duration,)
    error = proto.Field(proto.MESSAGE, number=13, message=status_pb2.Status,)
    source_database = proto.Field(proto.MESSAGE, number=14, message="DatabaseType",)
    destination_database = proto.Field(
        proto.MESSAGE, number=15, message="DatabaseType",
    )
    end_time = proto.Field(proto.MESSAGE, number=16, message=timestamp_pb2.Timestamp,)


class ConnectionProfile(proto.Message):
    r"""A connection profile definition.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The name of this connection profile resource
            in the form of
            projects/{project}/locations/{location}/instances/{instance}.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created. A timestamp in RFC3339 UTC "Zulu"
            format, accurate to nanoseconds. Example:
            "2014-10-02T15:01:23.045123456Z".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was last updated. A timestamp in RFC3339 UTC
            "Zulu" format, accurate to nanoseconds. Example:
            "2014-10-02T15:01:23.045123456Z".
        labels (Sequence[google.cloud.clouddms_v1.types.ConnectionProfile.LabelsEntry]):
            The resource labels for connection profile to use to
            annotate any related underlying resources such as Compute
            Engine VMs. An object containing a list of "key": "value"
            pairs.

            Example:
            ``{ "name": "wrench", "mass": "1.3kg", "count": "3" }``.
        state (google.cloud.clouddms_v1.types.ConnectionProfile.State):
            The current connection profile state (e.g.
            DRAFT, READY, or FAILED).
        display_name (str):
            The connection profile display name.
        mysql (google.cloud.clouddms_v1.types.MySqlConnectionProfile):
            A MySQL database connection profile.

            This field is a member of `oneof`_ ``connection_profile``.
        postgresql (google.cloud.clouddms_v1.types.PostgreSqlConnectionProfile):
            A PostgreSQL database connection profile.

            This field is a member of `oneof`_ ``connection_profile``.
        cloudsql (google.cloud.clouddms_v1.types.CloudSqlConnectionProfile):
            A CloudSQL database connection profile.

            This field is a member of `oneof`_ ``connection_profile``.
        error (google.rpc.status_pb2.Status):
            Output only. The error details in case of
            state FAILED.
        provider (google.cloud.clouddms_v1.types.DatabaseProvider):
            The database provider.
    """

    class State(proto.Enum):
        r"""The current connection profile state (e.g. DRAFT, READY, or
        FAILED).
        """
        STATE_UNSPECIFIED = 0
        DRAFT = 1
        CREATING = 2
        READY = 3
        UPDATING = 4
        DELETING = 5
        DELETED = 6
        FAILED = 7

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    state = proto.Field(proto.ENUM, number=5, enum=State,)
    display_name = proto.Field(proto.STRING, number=6,)
    mysql = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="connection_profile",
        message="MySqlConnectionProfile",
    )
    postgresql = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="connection_profile",
        message="PostgreSqlConnectionProfile",
    )
    cloudsql = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="connection_profile",
        message="CloudSqlConnectionProfile",
    )
    error = proto.Field(proto.MESSAGE, number=7, message=status_pb2.Status,)
    provider = proto.Field(proto.ENUM, number=8, enum="DatabaseProvider",)


class MigrationJobVerificationError(proto.Message):
    r"""Error message of a verification Migration job.

    Attributes:
        error_code (google.cloud.clouddms_v1.types.MigrationJobVerificationError.ErrorCode):
            Output only. An instance of ErrorCode
            specifying the error that occurred.
        error_message (str):
            Output only. A formatted message with further
            details about the error and a CTA.
        error_detail_message (str):
            Output only. A specific detailed error
            message, if supplied by the engine.
    """

    class ErrorCode(proto.Enum):
        r"""A general error code describing the type of error that
        occurred.
        """
        ERROR_CODE_UNSPECIFIED = 0
        CONNECTION_FAILURE = 1
        AUTHENTICATION_FAILURE = 2
        INVALID_CONNECTION_PROFILE_CONFIG = 3
        VERSION_INCOMPATIBILITY = 4
        CONNECTION_PROFILE_TYPES_INCOMPATIBILITY = 5
        NO_PGLOGICAL_INSTALLED = 7
        PGLOGICAL_NODE_ALREADY_EXISTS = 8
        INVALID_WAL_LEVEL = 9
        INVALID_SHARED_PRELOAD_LIBRARY = 10
        INSUFFICIENT_MAX_REPLICATION_SLOTS = 11
        INSUFFICIENT_MAX_WAL_SENDERS = 12
        INSUFFICIENT_MAX_WORKER_PROCESSES = 13
        UNSUPPORTED_EXTENSIONS = 14
        UNSUPPORTED_MIGRATION_TYPE = 15
        INVALID_RDS_LOGICAL_REPLICATION = 16
        UNSUPPORTED_GTID_MODE = 17
        UNSUPPORTED_TABLE_DEFINITION = 18
        UNSUPPORTED_DEFINER = 19
        CANT_RESTART_RUNNING_MIGRATION = 21

    error_code = proto.Field(proto.ENUM, number=1, enum=ErrorCode,)
    error_message = proto.Field(proto.STRING, number=2,)
    error_detail_message = proto.Field(proto.STRING, number=3,)


__all__ = tuple(sorted(__protobuf__.manifest))
