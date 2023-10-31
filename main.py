import time
import pytest
from memory_profiler import profile
from contextlib import contextmanager


# Dekorator do mierzenia czasu wykonywania funkcji
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper


# Generator generujący liczby parzyste
@profile
def even_numbers_generator(n):
    return (i for i in range(2, n + 1, 2))


# Funkcja zwracająca listę liczb parzystych
@profile
def even_numbers_function(n):
    return [i for i in range(2, n + 1, 2)]


# testy wydajności
def test_even_numbers_generator():
    n = 100000
    start_time = time.time()
    list(even_numbers_generator(n))
    end_time = time.time()
    assert end_time - start_time < 1.0  # Sprawdź, czy generowanie trwa krócej niż 1 sekunda


def test_even_numbers_function():
    n = 100000
    start_time = time.time()
    even_numbers_function(n)
    end_time = time.time()
    assert end_time - start_time < 1.0  # Sprawdź, czy generowanie trwa krócej niż 1 sekunda


@contextmanager
def timing_context_manager():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Code block executed in {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    n = 100000  # Liczba parzysta

    # Porównaj generator z funkcją używając dekoratora
    print("Using decorator:")
    even_numbers_gen = timing_decorator(even_numbers_generator)
    even_numbers_func = timing_decorator(even_numbers_function)

    even_numbers_gen(n)
    even_numbers_func(n)

    # Porównaj generator z funkcją używając context managera
    print("Using context manager:")
    with timing_context_manager():
        even_numbers_gen(n)
    with timing_context_manager():
        even_numbers_func(n)

    pytest.main()