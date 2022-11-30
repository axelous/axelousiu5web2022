import {Link} from "react-router-dom";

export const UserCard = ({idUser, name, surname}) => {
    return <Link to={`/profile/${idUser}`} className="text-blue-700 font-semibold p-2">{name} {surname}</Link>
}