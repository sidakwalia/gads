# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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


__protobuf__ = proto.module(
    package="google.ads.googleads.v7.services",
    marshal="google.ads.googleads.v7",
    manifest={"GetHotelGroupViewRequest",},
)


class GetHotelGroupViewRequest(proto.Message):
    r"""Request message for
    [HotelGroupViewService.GetHotelGroupView][google.ads.googleads.v7.services.HotelGroupViewService.GetHotelGroupView].

    Attributes:
        resource_name (str):
            Required. Resource name of the Hotel Group
            View to fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1,)


__all__ = tuple(sorted(__protobuf__.manifest))