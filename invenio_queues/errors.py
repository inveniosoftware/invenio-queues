# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2022 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Errors used in Invenio-Queues."""


class DuplicateQueueError(Exception):
    """Error raised when a duplicate queue is detected."""
