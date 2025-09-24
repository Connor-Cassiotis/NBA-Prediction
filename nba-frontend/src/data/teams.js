export const NBA_TEAMS = [
  { value: "ATL", label: "Atlanta Hawks", city: "Atlanta" },
  { value: "BOS", label: "Boston Celtics", city: "Boston" },
  { value: "BRK", label: "Brooklyn Nets", city: "Brooklyn" },
  { value: "CHA", label: "Charlotte Hornets", city: "Charlotte" },
  { value: "CHI", label: "Chicago Bulls", city: "Chicago" },
  { value: "CLE", label: "Cleveland Cavaliers", city: "Cleveland" },
  { value: "DAL", label: "Dallas Mavericks", city: "Dallas" },
  { value: "DEN", label: "Denver Nuggets", city: "Denver" },
  { value: "DET", label: "Detroit Pistons", city: "Detroit" },
  { value: "GSW", label: "Golden State Warriors", city: "Golden State" },
  { value: "HOU", label: "Houston Rockets", city: "Houston" },
  { value: "IND", label: "Indiana Pacers", city: "Indiana" },
  { value: "LAC", label: "LA Clippers", city: "LA" },
  { value: "LAL", label: "Los Angeles Lakers", city: "Los Angeles" },
  { value: "MEM", label: "Memphis Grizzlies", city: "Memphis" },
  { value: "MIA", label: "Miami Heat", city: "Miami" },
  { value: "MIL", label: "Milwaukee Bucks", city: "Milwaukee" },
  { value: "MIN", label: "Minnesota Timberwolves", city: "Minnesota" },
  { value: "NOP", label: "New Orleans Pelicans", city: "New Orleans" },
  { value: "NYK", label: "New York Knicks", city: "New York" },
  { value: "OKC", label: "Oklahoma City Thunder", city: "Oklahoma City" },
  { value: "ORL", label: "Orlando Magic", city: "Orlando" },
  { value: "PHI", label: "Philadelphia 76ers", city: "Philadelphia" },
  { value: "PHX", label: "Phoenix Suns", city: "Phoenix" },
  { value: "POR", label: "Portland Trail Blazers", city: "Portland" },
  { value: "SAC", label: "Sacramento Kings", city: "Sacramento" },
  { value: "SAS", label: "San Antonio Spurs", city: "San Antonio" },
  { value: "TOR", label: "Toronto Raptors", city: "Toronto" },
  { value: "UTA", label: "Utah Jazz", city: "Utah" },
  { value: "WAS", label: "Washington Wizards", city: "Washington" }
];

// Helper function to get team by value
export const getTeamByValue = (value) => {
  return NBA_TEAMS.find(team => team.value === value);
};

// Helper function to get all team values
export const getTeamValues = () => {
  return NBA_TEAMS.map(team => team.value);
};