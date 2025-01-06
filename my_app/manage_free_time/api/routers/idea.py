from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from dependency_injector.wiring import Provide, inject

from manage_free_time.container import Container
from manage_free_time.core.domain.idea import Idea, IdeaIn
from manage_free_time.infrastructure.services.idea import IIdeaService

router = APIRouter()

@router.get("/losowy", response_model=Idea)
@inject
async def get_random_idea(
    kategoria: str = Query(None, description="Kategoria pomysłu"),
    serwis: IIdeaService = Depends(Provide[Container.idea_service]),
) -> Idea:
    """
    Endpoint do pobierania losowego pomysłu.

    Args:
        kategoria (str): Kategoria, z której ma zostać wybrany pomysł.
        serwis (IIdeaService): Wstrzyknięta zależność serwisu pomysłów.

    Returns:
        Idea: Szczegóły losowego pomysłu.
    """
    idea = await serwis.get_random_idea(kategoria=kategoria)
    if not idea:
        raise HTTPException(status_code=404, detail="Pomysł nie został znaleziony")
    return idea


@router.post("/dodaj", response_model=Idea, status_code=201)
@inject
async def add_idea(
    nowy_pomysl: IdeaIn,
    serwis: IIdeaService = Depends(Provide[Container.idea_service]),
) -> Idea:
    """
    Endpoint do dodawania nowego pomysłu.

    Args:
        nowy_pomysl (IdeaIn): Dane nowego pomysłu.
        serwis (IIdeaService): Wstrzyknięta zależność serwisu pomysłów.

    Returns:
        Idea: Szczegóły dodanego pomysłu.
    """
    dodany_pomysl = await serwis.add_idea(nowy_pomysl)
    return dodany_pomysl


@router.get("/wszystkie", response_model=List[Idea])
@inject
async def get_all_ideas(
    serwis: IIdeaService = Depends(Provide[Container.idea_service]),
) -> List[Idea]:
    """
    Endpoint do pobierania wszystkich pomysłów.

    Args:
        serwis (IIdeaService): Wstrzyknięta zależność serwisu pomysłów.

    Returns:
        List[Idea]: Lista wszystkich pomysłów.
    """
    pomysly = await serwis.get_all_ideas()
    return pomysly


@router.get("/kategoria/{kategoria}", response_model=List[Idea])
@inject
async def get_ideas_by_category(
    kategoria: str,
    serwis: IIdeaService = Depends(Provide[Container.idea_service]),
) -> List[Idea]:
    """
    Endpoint do pobierania pomysłów według kategorii.

    Args:
        kategoria (str): Nazwa kategorii.
        serwis (IIdeaService): Wstrzyknięta zależność serwisu pomysłów.

    Returns:
        List[Idea]: Lista pomysłów w danej kategorii.
    """
    pomysly = await serwis.get_ideas_by_category(kategoria)
    return pomysly
