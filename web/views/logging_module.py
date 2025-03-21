from django.shortcuts import HttpResponse
import logging


logger = logging.getLogger('web')

def logging_module_practice(request):
    logger.debug('This is a debug message.')
    # logger.info('This is an info message.')
    # logger.warning('This is a warning message.')
    # logger.error('This is an error message.')
    # logger.critical('This is a critical message.')

    return HttpResponse('h')

def logging_module_practice_settings(request):
    logger.debug('This is a debug message.')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')
    return HttpResponse('h')