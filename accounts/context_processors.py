# myapp/context_processors.py
import os
from django.conf import settings

def versioned_static(request):
    version = 'v1.1'  # Increment this version number as needed
    return {
        'STATIC_VERSION': version,
    }
