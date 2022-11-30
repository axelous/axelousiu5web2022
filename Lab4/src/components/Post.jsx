import {Link} from "react-router-dom";

export const Post = ({idPost, photo}) => {
    return <Link to={`/post/${idPost}`}><img src={photo} className="w-[400px] h-[400px] object-cover"/></Link>
}