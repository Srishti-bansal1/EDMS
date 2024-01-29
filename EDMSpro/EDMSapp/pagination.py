from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4
    
    
    '''def get_page_number(self, request, paginator):  #custom page_num overrid the in-built page_num fun
        """
        Get the page number from the request's query parameters.
        """
        print(paginator)
        page_number = request.query_params.get(self.page_query_param, 1)
        try:
            return int(page_number)
        except ValueError:
            return'''
    


